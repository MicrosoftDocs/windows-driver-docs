---
title: Integration with Windows
author: windows-driver-content
description: Integration with Windows
MS-HAID:
- 'di\_0c0a93ad-ffca-4be9-9831-48550dd703aa.xml'
- 'hid.integration\_with\_windows'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 57721e38-5974-4080-b051-93b78a7f42c6
keywords: ["property sheets WDK DirectInput , registering", "game controllers WDK DirectInput , registrations", "control panels WDK DirectInput , registrations", "property sheets WDK DirectInput , Windows integration", "game controllers WDK DirectInput , Windows integration", "control panels WDK DirectInput , Windows integration", "Windows integration WDK DirectInput control panel", "registering property sheets", "registering devices for DirectInput control panel"]
---

# Integration with Windows


## <a href="" id="ddk-integration-with-windows-di"></a>


Because the property sheet page is a COM object, it needs to be registered. This can be done by an INF file or through DirectInput's **IDirectInputJoyConfig8** interface. A sample INF file is part of the sample property sheet in the DirectX Driver Development Kit (DDK).

**To register the property sheet page:**

1.  Use the GuidGen tool (which is included in the Microsoft Windows SDK) to create a CLSID for your property sheet (this is the same as the one entered in the **ConfigCLSID** entry mentioned earlier). Remember, this is your device-specific property sheet GUID and it should be the same as the one in your code.

2.  Create a new key in the registry under **My Computer\\HKEY\_CLASSES\_ROOT\\CLSID** using this new GUID (it should look something like {B9EA2BE1-E8E9-11D0-9880-00AA0044480F}).

3.  Inside that key, create subkeys named **InProcHandler32** and **InProcServer32**.

4.  Inside the **InProcServer32** key, edit the (default) entry to reflect the location and name of your property sheet DLL.

Your device must also be properly registered as a gaming device. This may be done through DirectInput, or through an INF file.

**To register the device:**

1.  In the registry key **My Computer\\HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\control\\MediaProperties\\PrivateProperties\\Joystick\\OEM**, enter a key for your device. It is advisable to make this key name the same as your device OEM Name.

2.  Create the following entries:

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Key Value</th>
    <th>Key value type</th>
    <th>Key value type contents</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>ConfigCLSID</p></td>
    <td><p>String Value</p></td>
    <td><p>&quot;{your property sheet CLSID}&quot;</p></td>
    </tr>
    <tr class="even">
    <td><p>OEMName</p></td>
    <td><p>String Value</p></td>
    <td><p>&quot;Product name of your device&quot;</p></td>
    </tr>
    </tbody>
    </table>

     

**Note**   These two entries are the minimum you need to get started. Refer to the DirectX DDK for additional information about all of the available entries and their associated services.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Integration%20with%20Windows%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


