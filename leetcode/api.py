import requests

import structs
import textwrap


def question_of_today() -> dict:
    return requests.post(
        "https://leetcode-cn.com/graphql",
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        json={
            "operationName": "questionOfToday",
            "variables": {},
            "query": """
query questionOfToday {
  todayRecord {
    date
    userStatus
    question {
      questionId
      frontendQuestionId: questionFrontendId
      difficulty
      title
      titleCn: translatedTitle
      titleSlug
      paidOnly: isPaidOnly
      freqBar
      isFavor
      acRate
      status
      solutionNum
      hasVideoSolution
      topicTags {
        name
        nameTranslated: translatedName
        id
      }
      extra {
        topCompanyTags {
          imgUrl
          slug
          numSubscribed
        }
      }
    }
    lastSubmission {
      id
    }
  }
}"""
        }
    ).json()


def format_note(data: dict, cn_tag=False) -> str:
    data = structs.DotDict(data).data

    # 直接从 chrome 获取 property path， 使用 Map 做了一层 dot 的封装

    def get_tags(translated=False) -> str:
        for tag in data.todayRecord[0].question.topicTags:
            if translated:
                yield tag.nameTranslated
            else:
                yield tag.name

    return textwrap.dedent(f"""\
        [{data.todayRecord[0].question.titleCn}](https://leetcode-cn.com/problems/{data.todayRecord[0].question.titleSlug})
        lc-no:: {data.todayRecord[0].question.questionId}
        lc-difficulty:: {data.todayRecord[0].question.difficulty}
        lc-tags:: {' '.join([f"[[{tag}]]" for tag in get_tags(cn_tag)])} 
        date:: [[{data.todayRecord[0].date.replace('-', '/')}]]
        type:: leetcode
        tags:: [[algorithm]]
        """)


if __name__ == '__main__':
    today = question_of_today()
    print(format_note(today, cn_tag=True))
