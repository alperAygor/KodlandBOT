import pytest
import db
import asyncio
import os 
folder_name="tests"
base_dir = os.path.dirname(os.path.abspath(__file__))
test_path = os.path.join(base_dir, "tests")

pytestmark = pytest.mark.asyncio

db.ExecuteDatabase()

if __name__ == "__main__":
    pytest.main([test_path])  # 'test' klasöründeki tüm test dosyalarını çalıştırır
