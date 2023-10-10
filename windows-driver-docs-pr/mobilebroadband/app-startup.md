---
title: App startup
description: App startup
ms.date: 04/20/2017
---

# App startup


When the mobile broadband app is started, it should check whether Internet access is available. The app can use an API to discover the various states of Internet connectivity. The app can then determine whether it can access back-end data when the Internet connection is in a “walled garden” state. If there is no Internet connection, the app should show an appropriate message or offline experience to the user.

If multiple operators’ subscriber identity modules (SIMs) are attached to the PC, the app can determine this. The app must present a user interface that works for multiple connected operator devices or accounts.

For example, the app can read the IMSI and IMEI information from the mobile broadband device. This information can be used as part of the authentication scheme, in addition or in place of a logon screen that sends user-name and password information to the back-end. Windows provides an API to securely store user-name and password information that the app can subsequently use for authentication after the first logon attempt. All user-name and password information must be exchanged with the operator back-end over Secure HTTP (HTTPS).

## Related topics


[Mobile broadband app scenarios](./account-management.md)

 

