import gym

#%% 환경 생성 및 초기화
env = gym.make("CartPole-v1")

#%% 시작 전 환경 재설정
env.reset()

#%% 게임 실행
for i in range(1000):
    # 변수 초기화
    done = False # 종료 변수
    game_rew = 0 # 보상
    
    while not done:
        # 랜덤 액션 선택
        action = env.action_space.sample()
        # 환경 내 한 개의 스텝
        obs, rew, done, info = env.step(action)
        # 보상 계산
        game_rew += rew
        # 게임 렌더링
        env.render()
        
        if done:
            print(f"Episode {i} finished, reward:{game_rew}")
            env.reset()

#%% 환경 종료
env.close()