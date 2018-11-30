from faker.providers import BaseProvider
from faker import Faker
from models import Market, Member, Consumer, Contract
"""How to use
----------------
fake = Faker('ko_KR')
fake.add_provider(MarketProvider)
fake.add_provider(MemberProvider)
fake.add_provider(ConsumerProvider)
fake.add_provider(ContractProvider)

market = fake.market()
print(market.studio_name, market.posts, market.working_time)
-----------------
"""

class MarketProvider(BaseProvider):
    def market(self):
        fake  = Faker('ko_KR')
        studio_name = fake.company()
        # posts = fake.text()
        posts = ""
        working_time = None
        costs = fake.pyint()
        kakao_id = fake.user_name()
        photographer_idx = fake.pyint()
        contract_idxs = [] # array of contract idx(int)
        tags = []
        location = fake.address()
        phone = fake.phone_number()
        return Market(studio_name, posts, working_time,
                      costs, kakao_id, photographer_idx,
                      contract_idxs, tags, location, phone)

class MemberProvider(BaseProvider):
    def member(self):
        fake  = Faker('ko_KR')
        member_type = fake.pyint() % 2
        consumer_idx = fake.pyint()
        photographer_idx = fake.pyint()
        return Member(member_type, consumer_idx,
                      photogrpher_idx)

class ConsumerProvider(BaseProvider):
    def consumer(self):
        fake  = Faker('ko_KR')
        member_idx = fake.pyint()
        contracts = [] # array of contract idx(int)
        return Consumer(member_idx, contracts)

class PhotographerProvider(BaseProvider):
    def photographer(self):
        fake  = Faker('ko_KR')
        markets = [] # array of market idx(int)
        member_idx = fake.pyint()
        return  Photographer(markets, member_idx)


class ContractProvider(BaseProvider):
    def contract(self):
        fake  = Faker('ko_KR')
        market_idx = fake.pyint()
        consumer_idx = fake.pyint()
        start_time = None
        end_time = None
        return Contract(market_idx, consumer_idx,
                        start_time, end_time)


if __name__ == '__main__':
    fake = Faker('ko_KR')
    fake.add_provider(MarketProvider)
    fake.add_provider(MemberProvider)
    fake.add_provider(ConsumerProvider)
    fake.add_provider(ContractProvider)

    market = fake.market()
    print(market.studio_name, market.posts, market.working_time)

