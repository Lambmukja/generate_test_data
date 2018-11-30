# 테스트 데이터 생성
## 데이터 생성 방법
```python
from faker import Faker
from providers import (
  MarketProvider, MemberProvider,
  ConsumerProvider, ContractProvider
)


fake = Faker('ko_KR')
# If you want to generate 'Market' model
fake.add_provider(MarketProvider)
market = fake.market()
# If you want to generate 'Member' model
fake.add_provider(MemberProvider)
member = fake.member()
# If you want to generate 'Consumer' model
fake.add_provider(ConsumerProvider)
consumer = fake.consumer()
# If you want to generate 'Contract' model
fake.add_provider(ContractProvider)
contract = fake.contract()
```
