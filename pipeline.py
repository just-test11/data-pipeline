"""Nightly ETL entry point."""


def extract(source):
    return [{"id": i, "amount": i * 10} for i in range(source)]


def transform(rows):
    return [r for r in rows if r["amount"] > 0]


def load(rows):
    print(f"loaded {len(rows)} rows")
    return len(rows)


def main():
    return load(transform(extract(5)))


if __name__ == "__main__":
    main()
