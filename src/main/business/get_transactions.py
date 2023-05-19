from faker import Faker
fake = Faker()
import random


def get_transactions():
    entries = []
    for _ in range(1000):
        entry = {
            'id': fake.uuid4(),
            'transaction_type': fake.word(),
            'remote_id': fake.uuid4(),
            'remote_data': fake.text(max_nb_chars=128),
            'number': fake.random_number(digits=8),
            'transaction_date': fake.date(),
            'account': f"{random.randint(0,9)}",
            'contact': fake.name(),
            'total_amount': fake.random_number(digits=4),
            'currency': fake.currency_code(),
            'remote_was_deleted': fake.boolean(),
        }
        entries.append(entry)
    return entries
