import gym

#%% 환경 생성 및 초기화
env = gym.make("CartPole-v1")

#%% 관측 공간의 유형과 차원
print(env.observation_space)

#%% 액션 공간의 유형과 차원
print(env.action_space)

#%% 액션의 종류
'''
CartPole 에서
0 : 왼쪽
1 : 오른쪽
'''
print(env.action_space.sample())
print(env.action_space.sample())

#%% Box 공간에서 허용되는 최솟값과 최댓값
print(env.observation_space.low)
print(env.observation_space.high)
