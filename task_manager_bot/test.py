import pytest
import db
import asyncio
pytestmark = pytest.mark.asyncio
db.ExecuteDatabase()
if __name__ == "__main__":
    pytest.main(["tests"])  # 'test' klasöründeki tüm test dosyalarını çalıştırır
