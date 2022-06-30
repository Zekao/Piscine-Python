languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
def main(): 
    for dict in languages.items():
        print(list(dict)[0], "was created by", list(dict)[1])

if __name__=="__main__":
    main()