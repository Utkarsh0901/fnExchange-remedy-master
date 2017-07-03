import requests
from fnexchange.core.plugins import AbstractPlugin

class RemedyPlugin(AbstractPlugin):
#class RemedyPlugin():

    def get_token(self, payload):
	
	login_info = {"username":self.config.username,"password":self.config.password}
        token_created = False
        try:
            token = requests.post(self.config.url_login, data = login_info)
            token_created = response.status_code == 200
        except:
            pass
        return token,token_created

    def revoke_token(self,token):
        logged_out = False
        try:
            response = requests.post(self.config.url_logout, auth = token)
            logged_out = response.status_code == 204
        except:
            pass

        return logged_out


    def post_ticket(self, payload):
        token,token_created = get_token(payload)
	token = "AR-JWT " + token

        ticket_posted = False
        try:
            response = requests.post(self.config.url_post_ticket, json = payload['elements'][0], auth = token)
            ticket_posted = response.status_code == 201
        except:
            pass

        logged_out = revoke_token(token)

        return {
            'metadata': {[
                'token created ' = token_created,
                '\nticket posted ' = ticket_posted,
                '\nlogged out ' = logged_out
                ]},
            'elements': payload['elements'][0]
        }

    def get_ticket(self, payload):
        token,token_created = get_token(payload)
	token = "AR-JWT " + token        
	formName = payload['elements']['formName']
        entryID = paylaod['elements']['entryID']
	
	url = self.config.url_get_tickEt + '/' + formName + '/' + entryID
        ticket_got = False
        try:
            elements = requests.get(url, auth = token)
            ticket_got = elements.status_code == 200
        except:
            pass

        logged_out = revoke_token(token)

        return {
            'metadata': {[
                'token created ' : token_created
                '\ngot ticket ': ticket_got
                '\nlogged out ' : logged_out
            ]},
            'elements': elements
        }

    def delete_ticket(self, payload):
        token,token_created = get_token(payload)
	token = "AR-JWT " + token        
	formName = payload['elements']['formName']
        entryID = paylaod['elements']['entryID']
        ticket_deleted = False
        url = self.config.url_delete_tickEt + '/' + formName + '/' + entryID

        try:
            deleted = requests.delete(url, auth = token)
            ticket_deleted = elements.status_code == 204
        except:
            pass

        logged_out = revoke_token(token)

        return {
            'metadata': {[
                'token created ' : token_created
                '\ndeleted ticket ': ticket_deleted
                '\nlogged out ' : logged_out
            ]},
            'elements': deleted
        }

    def update_ticket(self, payload):
        token,token_created = get_token(payload)
	token = "AR-JWT " + token
        formName = payload['elements']['formName']
        entryID = paylaod['elements']['entryID']
        ticket_updated = False
        url = self.config.url_update_tickEt + '/' + formName + '/' + entryID

        try:
            updated = requests.put(url, auth = token)
            ticket_updated = elements.status_code == 204
        except:
            pass

        logged_out = revoke_token(token)

        return {
            'metadata': {[
                'token created ' : token_created
                '\nupdated ticket ': ticket_updated
                '\nlogged out ' : logged_out
            ]},
            'elements': updated
        }



'''
username and password taken from config file
zeroth element of list of "elements" should be formName and entryID then the first should be values and all for all whereever required
payload format for posting ticket is given in README.md
paylaod format for deleting and updating ticket has to give {"elements":[{"formName":"name of form",'entryID':'entryID'}]}, formName and entry ID can be taken from running get.
in delete, if entryID is not mentioned it will delete everything or get every result
'''
'''
first element of payload format can be seen from Purpose Order or line item for posting ticket
'''
#payload = {"elements":[{},{"vales":{Submitter:"Donkey"},{"Short Description":"Monitor is cracked"}}],"metadata":{}}

#print RemedyPlugin().post_ticket(payload)

