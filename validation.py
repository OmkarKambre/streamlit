import streamlit as st
import yaml
import paramiko

with open("config.yaml", "r") as f:
    validation_rules = yaml.safe_load(f)["validation_rules"]

st.title("Validation Tool")

ip_input = st.text_input("Enter IP or Hostname:")
username_input = st.text_input("Enter username:")
password_input = st.text_input("Enter password:", type="password")
port_input = st.number_input("Enter port:", value=22)
platform_input = st.selectbox("Select platform:", ["linux", "android", "windows"])

def run_validation(ip, username, password, port, platform):
    results = {}

    platform_rules = [rule for rule in validation_rules if rule["platform"] == platform]

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password, port=port, timeout=30)
    except paramiko.SSHException as e:
        st.error(f"SSH connection failed: {e}")
        return

    for rule in platform_rules:
        rule_name = rule["rule_name"]
        versions = rule["version"].split("|")
        command = rule["command"]

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()

        if output in versions:
            result = "PASS"
        else:
            result = "FAILED"

        results[rule_name] = {"result": result, "command": command, "version": output}

    

    st.write("Results:")
    st.write("IP | Rule name | Result | Command | Version")
    for rule_name, result in results.items():
        st.write(f"{ip} | {rule_name} | {result['result']} | {result['command']} | {result['version']}")

    ssh.close()

# Button to run validation
if st.button("Run Validation"):
    run_validation(ip_input, username_input, password_input, port_input, platform_input)