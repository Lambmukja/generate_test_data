from faker.providers import BaseProvider
from faker import Factory


class Market:
    def __init__(self, studio_name, posts, working_time,
                 costs, kakao_id, photographer_idx,
                 contract_idxs, tags, location, phone):
        self.studio_name = studio_name
        self.posts = posts
        self.working_time = working_time
        self.costs = costs
        self.kakao_id = kakao_id
        self.photographer_idx = photographer_idx
        self.contract_idxs = contract_idxs
        self.tags = tags
        self.location = location
        self.phone = phone


class Member:
    def __init__(self, member_type, consumer_idx,
                 photographer_idx):
        self.member_type = member_type
        self.consumer_idx = consumer_idx
        self.photographer_idx = photographer_idx


class Consumer:
    def __init__(self, member_idx, contracts):
        self.member_idx = member_idx
        self.contracts = contracts


class Photographer:
    def __init__(self, markets, member_idx):
        self.markets = markets
        self.member_idx = member_idx


class Contract:
    def __init__(self, market_idx, consumer_idx,
                 start_time, end_time):
        self.market_idx = market_idx
        self.consumer_idx = consumer_idx
        self.start_time = start_time
        self.end_time = end_time


if __name__ == '__main__':
    pass
