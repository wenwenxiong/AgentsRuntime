#!/usr/bin/env python3
# 测试脚本
import os
import sys

# 强制输出到文件
log_file = "/tmp/test_output.txt"
with open(log_file, "w") as f:
    f.write("Test script started\n")
    f.write(f"Python version: {sys.version}\n")
    f.write(f"Current directory: {os.getcwd()}\n")

    try:
        import generate_agent_profiles

        f.write("Module imported successfully\n")

        # 测试 openclaw 配置
        openclaw_agent = [
            a for a in generate_agent_profiles.AGENTS_CONFIG if a["id"] == "openclaw"
        ][0]
        f.write(f"Openclaw agent found: {openclaw_agent}\n")
        f.write(f"Skills list: {openclaw_agent['skills']}\n")

        # 测试 generate_user 函数
        user_md = generate_agent_profiles.generate_user(openclaw_agent)
        f.write(f"USER.md generated, length: {len(user_md)}\n")

        # 查找技能清单部分
        lines = user_md.split("\n")
        f.write("Searching for skills section...\n")
        for i, line in enumerate(lines):
            if "我的技能清单" in line:
                f.write(f"Found skills section at line {i}\n")
                f.write("Skills section content:\n")
                for j in range(i, min(i + 30, len(lines))):
                    f.write(f"  {j}: {lines[j]}\n")
                break
        else:
            f.write("Skills section not found!\n")

        # 写入测试文件
        test_file = "workspace/test_user_md.txt"
        os.makedirs("workspace", exist_ok=True)
        with open(test_file, "w", encoding="utf-8") as tf:
            tf.write(user_md)
        f.write(f"Test file written to: {test_file}\n")

        # 调用 main 函数
        f.write("Calling main() function...\n")
        generate_agent_profiles.main()
        f.write("main() function completed\n")

    except Exception as e:
        f.write(f"Error occurred: {e}\n")
        import traceback

        f.write(traceback.format_exc())

    f.write("Test script completed\n")

print(f"Test completed. Check {log_file} for details.")
