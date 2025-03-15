import subprocess
import sys

result: subprocess.CompletedProcess[str] = subprocess.run(
    ["poetry", "run", "mypy", "."], capture_output=True, text=True
)

print(result.stdout)  # noqa
print(result.stderr, file=sys.stderr)  # noqa

sys.exit(result.returncode)
