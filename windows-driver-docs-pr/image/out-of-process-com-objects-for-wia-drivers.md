---
title: Out-of-Process COM Objects for WIA Drivers
description: Out-of-Process COM Objects for WIA Drivers
ms.assetid: 0b08652e-36ae-46f8-8915-7f2bb45df05c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Out-of-Process COM Objects for WIA Drivers





If a driver calls **CoCreatInstance** (described in the Microsoft Windows SDK documentation) on an out-of-process component, that call will fail unless the component has the appropriate permissions set to allow the driver access.

Consult COM programming books or the online documentation for detailed information about COM's security model. Following is a brief explanation.

There are two kinds of permissions associated with out-of-process COM components:

-   Launch permissions

    Launch permissions indicate who has permission to start up the COM component if it is not currently running. For example, if the component is implemented in a local server that is not running, calling **CoCreateInstance** for that component results in COM attempting to launch the local server (assuming the caller has permission to start it).

-   Access permissions

    Access permissions indicate who is allowed to call into that process to retrieve the COM interfaces to those COM components.

    Launch permissions and access permissions do not have to match. For example, launch permissions could be set to Administrators only, but access permissions could be set to Interactive Users and Administrators. Or, Administrators might be granted permission to start the COM server, but regular users would only be able to use the components if the COM server were already running.

A good practice is to store the launch and access permissions for your COM servers in the appropriate place under the component's **AppId** registry subkey. This allows Administrators to change those permissions if needed, using the Component Services management tool. To make your COM server use those access permissions at run time, be sure to call **CoInitializeSecurity** (described in the Windows SDK documentation) with the EOAC\_APPID flag, passing in the component's **AppId**. This causes COM to go to the component's **AppId** subkey in the registry and to use the permissions set in the **AccessPermission** and **LaunchPermission** entries.

 

 




