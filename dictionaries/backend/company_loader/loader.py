from utils.utils import initialize_django

initialize_django()

from backend.models import RegisteredCompany
import csv

statuses_data = {
    'Liquidation', 
    'RECEIVER MANAGER / ADMINISTRATIVE RECEIVER', 
    'Live but Receiver Manager on at least one charge', 
    'Active', 
    'In Administration/Administrative Receiver', 
    'In Administration/Receiver Manager', 
    'In Administration', 
    'ADMINISTRATION ORDER', 
    'ADMINISTRATIVE RECEIVER', 
    'RECEIVERSHIP', 
    'Active - Proposal to Strike off', 
    'Voluntary Arrangement'
}

def main():
    with open("data/UK_Company_Data_01.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        create_companies = 0
        statuses = set()
        line_count = 0
        column_names = []

        for row in csv_reader:
            if line_count == 0:
                column_names = row
                print(f'Column names are {", ".join(row)}')
            else :
                for column_name in column_names :  
                    print(f"row[{column_name}]", row[column_name])
                import pdb; pdb.set_trace()
                print('foo')
            line_count += 1

                # company_name = row["CompanyName"]
                # import pdb; pdb.set_trace()
                # is_active = True if row["CompanyStatus"] == "Active" else False

                # company_status = row["CompanyStatus"] 
                # print('status', company_status)
                # if company_status != "Active" :
                #     import pdb; pdb.set_trace()
                #     print('foo')
                
                # if company_status not in statuses :
                    # statuses.add(company_status)


        print('statuses', statuses)
        import pdb; pdb.set_trace()
            # if not is_active :
            #     company_db, created = RegisteredCompany.objects.get_or_create(name=company_name)
            #     company_db.is_active = False
            #     company_db.save()

            # try :
            #     company_db, created = RegisteredCompany.objects.get_or_create(name=company_name)
            # except Exception as e :
            #     print('foo', company_name)
            #     import pdb; pdb.set_trace()
            #     print('foo')
            # if created :
            #     create_companies += 1
                

        print(f'Created {create_companies} companies.')
                

if __name__ == "__main__":
    main()
