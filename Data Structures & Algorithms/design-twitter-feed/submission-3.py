class Twitter:

    def __init__(self):
        self.Posted = dict() ## Key User ID, values messages posted
        self.Following = dict() ## Key User ID, vals who they follow
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.Posted:
            messages = self.Posted[userId]
            messages.append((self.t,tweetId))
            if len(messages) > 10:
                messages.popleft()
            self.Posted[userId] = messages
        else:
            self.Posted[userId] = deque([(self.t, tweetId)])
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        Following = {userId}
        if userId in self.Following:
            Following = self.Following[userId]
            Following.add(userId)
        h = []
        for user in Following:
            if user in self.Posted:
                h.extend(self.Posted[user])
                heapq.heapify(h)
                h = heapq.nsmallest(10, h)
        return [item[1] for item in h]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.Following:
            self.Following[followerId].add(followeeId)
        else:
            self.Following[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.Following:
            if followeeId in self.Following[followerId]:
                self.Following[followerId].remove(followeeId)
