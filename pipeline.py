"""Nightly ETL entry point."""

from retry import with_retry


def extract(source):
    return [{"id": i, "amount": i * 10} for i in range(source)]


def transform(rows):
    return [r for r in rows if r["amount"] > 0]


def load(rows):
    print(f"loaded {len(rows)} rows")
    return len(rows)


def main():
    rows = transform(extract(5))
    return with_retry(lambda: load(rows))


if __name__ == "__main__":
    main()
