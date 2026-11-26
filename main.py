from pathlib import Path

# The entry: a single-line out-of-office auto-reply (83 characters).
ENTRY = "I'm out of office — my out-of-office is also out of office; please bother the void."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
