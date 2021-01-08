import math

public_repo = 16
contribution = 16
commit_sum = 455
issues = 0
pull_requests = 15
star_sum = 0
followers = 1

PUBLIC_REPO_OFFSET = 1.18
CONTRIBUTION_OFFSET = 1.16
COMMIT_OFFSET = 1.12
ISSUES_OFFSET = 1.13
PULL_REQUESTS_OFFSET = 1.10
STARS_OFFSET = 0.92
FOLLOWERS_OFFSET = 0.91

# 元のプログラムの値
# PUBLIC_REPO_OFFSET = 1
# CONTRIBUTION_OFFSET = 1.65
# COMMIT_OFFSET = 1.65
# ISSUES_OFFSET = 1
# PULL_REQUESTS_OFFSET = 0.5
# STARS_OFFSET = 0.75
# FOLLOWERS_OFFSET = 0.45
ALL_OFFSETS = PUBLIC_REPO_OFFSET+CONTRIBUTION_OFFSET+COMMIT_OFFSET+ISSUES_OFFSET + \
    PULL_REQUESTS_OFFSET+STARS_OFFSET+FOLLOWERS_OFFSET

RANK_S_VALUE = 1
RANK_DOUBLE_A_VALUE = 25
RANK_A2_VALUE = 45
RANK_A3_VALUE = 60
RANK_B_VALUE = 100
TOTAL_VALUES = RANK_S_VALUE + RANK_DOUBLE_A_VALUE + \
    RANK_A2_VALUE + RANK_A3_VALUE + RANK_B_VALUE

score = (
    public_repo*PUBLIC_REPO_OFFSET +
    contribution * CONTRIBUTION_OFFSET +
    commit_sum*COMMIT_OFFSET +
    issues * ISSUES_OFFSET +
    pull_requests * PULL_REQUESTS_OFFSET +
    star_sum * STARS_OFFSET +
    followers * FOLLOWERS_OFFSET
) / 100


def normalcdf(mean, sigma, to):
    z = (to - mean) / math.sqrt(2 * sigma * sigma)
    t = 1 / (1 + 0.3275911 * abs(z))
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    erf = 1 - ((((a5 * t + a4) * t + a3) * t + a2)
               * t + a1) * t * math.exp(-z * z)
    sign = 1
    if z < 0:
        sign = -1
    return (1 / 2) * (1 + sign * erf)


normalizedScore = normalcdf(score, TOTAL_VALUES, ALL_OFFSETS) * 100
print("score: ")
print(normalizedScore)
