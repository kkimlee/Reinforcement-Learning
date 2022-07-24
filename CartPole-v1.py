import gym

#%% 환경 생성 및 초기화
env = gym.make("CartPole-v1")

#%% 시작 전 환경 재설정
env.reset()

#%% 게임 실행
for i in range(500):
    # 랜덤 액션 선택
    env.step(env.action_space.sample())
    # 게임 렌더링
    env.render()

#%% 환경 종료
env.close()