import Engine as e

if __name__ == '__main__':
    dbconn = e.db('Engine/SurveyMaker')
    main = e.mv(dbconn)
    cs = e.csv(dbconn)
    sl = e.slv(dbconn)
    tas = e.tasv(dbconn)
    vc = e.vc(main, cs, sl, tas)
