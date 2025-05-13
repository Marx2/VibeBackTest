import subprocess

def test_end_to_end():
    """
    Test the end-to-end functionality of the VibeBackTest application.
    """
    try:
        # Run the main.py script with sample arguments
        result = subprocess.run(
            [
                "python3", "vibebacktest/vibebacktest/main.py",
                "--strategy", "vibebacktest/sample_strategy.yaml",
                "--start-date", "2023-01",
                "--end-date", "2023-12"
            ],
            capture_output=True,
            text=True
        )

        # Print the output for verification
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)

        # Check for errors
        assert result.returncode == 0, "The script failed with errors."

    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_end_to_end()