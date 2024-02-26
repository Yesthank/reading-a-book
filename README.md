링크!!!>>>>
https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K#

## Github에 계속 업데이트 하는법 🤹‍♂️
# 추가할 파일 더하기
git add .
# 히스토리 만들기
git commit -m "first commit"
# Github로 올리기
git push origin master


## Github로 팀프로젝트 하는법
# Github에서 소스코드 다운로드

git clone 주소 폴더이름
  주소는 깃허브에서 들고와야함
  폴더이름은 선택사항이다 (즉 없어도됨) 폴더이름을 줄경우에는 그 폴더가 새로 생성이 되면서 그 안에 코드들이 다운로드가 되고, 폴더이름을 안줄경우엔 깃허브 프로젝트 이름으로 폴더가 자동으로 생기고 그안에 코드들이 다운로드된다.

# Github에서 내 브렌치(branch)만들기

  git checkout -b 브렌치이름

# 내 브렌치에 소스코드 업데이트하기

  git add .
  git commit -m "first commit"
  git push origin 브렌치이름

# 마스터 브렌치에 소스 가져오기(pull)

  git pull origin master
pull을 하기전에는 기존에 소스코드들을 commit을 먼저 해놔야 한다 (2탄 강의참조)

# 브렌치끼리 이동하는 법

git checkout 브렌치이름
