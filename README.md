# fnExchange Remedy Plugin (under construction)
This is a plugin for the fnExchange API router for interacting with BMC-Remedy. <br/>

This plugin currently only provides an Action for posting and getting tickets from a Remedy channel using URL's. .<br/>

You can get the login URL [here](http://<server_name>:<port>/api/jwt/login) <br/>
You can get the post request URL [here](http://<server_name>:<port>/api/arsys/v1/entry/HPD:IncidentInterface_Create)<br/>
You can get the get request URL [here](//<server_name>:<port>/api/arsys/v1/entry)        {formName}{entryId} --- optional<br/>
You can get the delete request URL [here](http://<server_name>:<port>/api/arsys/v1/entry)     {formName}{entryId} --- necessary (unless you want to delete everything) <br/>
You can get the put request URL [here](http://<server_name>:<port>/api/arsys/v1/entry)         {formName}{entryId} --- necessary<br/>
You can get the logout URL [here](http://<server_name>:<port>/api/jwt/logout)
<br/><br/>
HPD:IncidentInterface_Create is a form name
<br/><br/>
form name and entry id for get,delete,put should be given in payload in elements first index
<br/><br/>
You can use the following forms:
<br/>
<br/>
    HPD:IncidentInterface_Create - to create or submit new incident <br/>
    HPD:IncidentInterface - to perform SEARCH,READ,UPDATE/MODIFY on existing incident <br/>
    CHG:ChangeInterface - to create change request <br/>
    CHG:ChangeInterface_Create - update and modify change request <br/>
    CHG:CRQ:Worklog - for work Info/log <br/>
    HPD:INC:Worklog - for Incident work log <br/>

```yaml
payload = 
{"elements":[
    {"formName":"name of form",'entryID':'entryID'},
    {"values" : {
         "First_Name" : "Allen" ,
         "Last_Name" : "Allbrook" ,
         "Description" : "REST API: Incident Creation" ,
         "Impact" : "1-Extensive/Widespread" ,
         "Urgency" : "1-Critical" ,
         "Status" : "Assigned" ,
         "Reported Source" : "Direct Input" ,
         "Service_Type" : "User Service Restoration" ,
         "z1D_Action" : "CREATE"}
    }
    }
    ]
}
```

# Installation
Simply install this as
```
$ pip install fnexchange-remedy (not available)
```

# Configuration
To use this plugin with fnExchange, add the appropriate configuration to the `fnexchange.yml`
configuration file under `plugins_enabled`. A sample configuration is provided below.
Of course, note that you can use any alias instead of "remedy".

The plugin **requires** the `url` configuration.

```yaml
...
  plugins_enabled:
    ...
    slacker:
      class_name: 'fnexchange_remedy.RemedyPlugin'
      config:
        url_login: 'login url'
        url_post_ticket: 'url where the ticket is to be posted'
        url_get_ticket: 'url from where the ticket is to be retrived'
        url_delete_ticket: 'url from where the ticket is to be is to be deleted'
        url_upgrade_ticket: 'url where to update ticket'
        url_logout: 'logout url'
    ...
...
```
