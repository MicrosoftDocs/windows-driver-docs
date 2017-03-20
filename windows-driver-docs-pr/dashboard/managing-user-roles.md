---
title: Managing User Roles
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 000D3756-7110-4E9F-91CA-86F91EECCFCA
description: 
---

# Managing User Roles


The Windows Hardware Dev Center Dashboard allows you to assign specific roles to each of your users. The following roles are available for dashboard users:

| Role                           | Description                                                                                                                                                                                                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrator                  | Has complete control of your organization. Can manage roles in Dev Center and can complete any task.                                                                                                                                                       |
| Upgrade Test Results Submitter | Can submit MDA upgrade test results for your organization.                                                                                                                                                                                                 |
| Legal Agreement Signer         | Can renew and sign legal agreements on behalf of your organization.                                                                                                                                                                                        |
| Report Reviewer                | Can access analytics about your drivers and systems. Able to see failure details and download cabs.                                                                                                                                                        |
| Driver Submitter               | Can create new driver submissions, but can’t create shipping labels.                                                                                                                                                                                       |
| Shipping Label Owner           | Can create and manage shipping labels, and can submit shipping labels that do not have driver promotions (automatic installation) selected. Can’t submit shipping labels that have driver promotions selected.                                             |
| Shipping Label Promoter        | Adds the additional ability to submit shipping labels that have driver promotions (automatic installation) selected. This role requires the Shipping Label Owner role. If you select this role, you must also give the user the Shipping Label Owner role. |
| System Submitter               | Can create new Systems Certifications and onboard new device definitions for the purposes of MDA Upgrade Test result uploads. Can’t make changes to driver submissions or shipping labels.                                                                 |

 

To change a user’s roles, navigate to the [Manage Users](https://go.microsoft.com/fwlink/?linkid=833569) section of **Account Settings**. Find the user you want to modify by using the search bar and click on their name.

![an image showing the manage users menu in the windows hardware dev center](images/manage-users.png)

In the user’s details, scroll down to the roles and select the ones they should have access to.

![an image showing the various roles available to users](images/user-roles.png)

Finalize your selections by selecting **Save**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Managing%20User%20Roles%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




