---
title: Out-of-Process COM Objects for WIA Drivers
description: Out-of-Process COM Objects for WIA Drivers
MS-HAID:
- 'WIA\_best\_practice\_84f531b7-45f2-4f6d-81ed-ca741f2ac430.xml'
- 'image.out\_of\_process\_com\_objects\_for\_wia\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0b08652e-36ae-46f8-8915-7f2bb45df05c
---

# Out-of-Process COM Objects for WIA Drivers


## <a href="" id="ddk-out-of-process-com-objects-for-wia-drivers-si"></a>


If a driver calls **CoCreatInstance** (described in the Microsoft Windows SDK documentation) on an out-of-process component, that call will fail unless the component has the appropriate permissions set to allow the driver access.

Consult COM programming books or the MSDN documentation for detailed information about COM's security model. Following is a brief explanation.

There are two kinds of permissions associated with out-of-process COM components:

-   Launch permissions

    Launch permissions indicate who has permission to start up the COM component if it is not currently running. For example, if the component is implemented in a local server that is not running, calling **CoCreateInstance** for that component results in COM attempting to launch the local server (assuming the caller has permission to start it).

-   Access permissions

    Access permissions indicate who is allowed to call into that process to retrieve the COM interfaces to those COM components.

    Launch permissions and access permissions do not have to match. For example, launch permissions could be set to Administrators only, but access permissions could be set to Interactive Users and Administrators. Or, Administrators might be granted permission to start the COM server, but regular users would only be able to use the components if the COM server were already running.

A good practice is to store the launch and access permissions for your COM servers in the appropriate place under the component's **AppId** registry subkey. This allows Administrators to change those permissions if needed, using the Component Services management tool. To make your COM server use those access permissions at run time, be sure to call **CoInitializeSecurity** (described in the Windows SDK documentation) with the EOAC\_APPID flag, passing in the component's **AppId**. This causes COM to go to the component's **AppId** subkey in the registry and to use the permissions set in the **AccessPermission** and **LaunchPermission** entries.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Out-of-Process%20COM%20Objects%20for%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




