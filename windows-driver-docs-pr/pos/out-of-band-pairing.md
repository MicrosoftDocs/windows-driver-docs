---
title: Out-of-band pairing
author: windows-driver-content
description: Out-of-band pairing allows apps to connect to a Point-of-Service peripheral without requiring discovery.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8814E511-6BD0-4427-A3E1-25574A09DAC2
---

# Out-of-band pairing


**Note**  This feature requires Windows 10, version 1511 or later.

 

Out-of-band pairing allows apps to connect to a Point-of-Service peripheral without requiring discovery. Apps must use the [**Windows.Devices.PointOfService**](https://msdn.microsoft.com/library/windows/apps/dn298071) namespace and pass in a specifically formatted string (out-of-band blob) to the appropriate **FromIdAsync** method for the desired peripheral. When **FromIdAsync** is executed, the host device pairs and connects to the peripheral before the operation returns to the caller.

## Out-of-band blob format


``` syntax
    "connectionKind":"Network",
    "physicalAddress":"AA:BB:CC:DD:EE:FF",
    "connectionString":"192.168.1.1:9001",
    "peripheralKinds":"{C7BC9B22-21F0-4F0D-9BB6-66C229B8CD33}",
    "providerId":"{02FFF12E-7291-4A5D-ADFA-DA8FB7769CD2}",
    "providerName":"PrinterProtocolProvider.dll"
```

<a href="" id="connectionkind"></a>*connectionKind*  
The type of connection. Valid values are "Network" and "Bluetooth".

<a href="" id="physicaladdress"></a>*physicalAddress*  
The MAC address of the peripheral. For example, in the case of a network printer, this would be the MAC address that is provided by the printer test sheet in AA:BB:CC:DD:EE:FF format.

<a href="" id="connectionstring"></a>*connectionString*  
The connection string of the peripheral. For example, in the case of a network printer, this would be the IP address provided by the printer test sheet in 192.168.1.1:9001 format. This field is omitted for all Bluetooth peripherals.

<a href="" id="peripheralkinds"></a>*peripheralKinds*  
The GUID for the device type. Valid values are:

|                 |                                      |
|-----------------|--------------------------------------|
| POS printer     | C7BC9B22-21F0-4F0D-9BB6-66C229B8CD33 |
| Barcode scanner | C243FFBD-3AFC-45E9-B3D3-2BA18BC7EBC5 |
| Cash drawer     | 772E18F2-8925-4229-A5AC-6453CB482FDA |

 

<a href="" id="providerid"></a>*providerId*  
The GUID for the protocol provider class. Valid values are:

|                                 |                                      |
|---------------------------------|--------------------------------------|
| Generic ESC/POS network printer | 02FFF12E-7291-4A5D-ADFA-DA8FB7769CD2 |
| Generic ESC/POS BT printer      | CCD5B810-95B9-4320-BA7E-78C223CAF418 |
| Epson BT printer                | 94917594-544F-4AF8-B53B-EC6D9F8A4464 |
| Epson network printer           | 9F0F8BE3-4E59-4520-BFBA-AF77614A31CE |
| Star network printer            | 1E3A32C2-F411-4B8C-AC91-CC2C5FD21996 |
| Socket BT scanner               | 6E7C8178-A006-405E-85C3-084244885AD2 |
| APG network drawer              | E619E2FE-9489-4C74-BF57-70AED670B9B0 |
| APG BT drawer                   | 332E6550-2E01-42EB-9401-C6A112D80185 |

 

<a href="" id="providername"></a>*providerName*  
The name of the provider DLL. The default providers are:

|             |                                    |
|-------------|------------------------------------|
| Printer     | PrinterProtocolProvider.dll        |
| Cash drawer | CashDrawerProtocolProvider.dll     |
| Scanner     | BarcodeScannerProtocolProvider.dll |

 

## Usage example: Network printer


```CSharp
       String oobBlobNetworkPrinter =
          "{\"connectionKind\":\"Network\"," +
          "\"physicalAddress\":\"AA:BB:CC:DD:EE:FF\"," +
          "\"connectionString\":\"192.168.1.1:9001\"," +
          "\"peripheralKinds\":\"{C7BC9B22-21F0-4F0D-9BB6-66C229B8CD33}\"," +
          "\"providerId\":\"{02FFF12E-7291-4A5D-ADFA-DA8FB7769CD2}\"," +
          "\"providerName\":\"PrinterProtocolProvider.dll\"}";
            
       printer = await PosPrinter.FromIdAsync(oobBlobNetworkPrinter);
```

## Usage example: Bluetooth printer


```CSharp
       string oobBlobBTPrinter =
            "{\"connectionKind\":\"Bluetooth\"," +
            "\"physicalAddress\":\"AA:BB:CC:DD:EE:FF\"," +
            "\"peripheralKinds\":\"{C7BC9B22-21F0-4F0D-9BB6-66C229B8CD33}\"," +
            "\"providerId\":\"{CCD5B810-95B9-4320-BA7E-78C223CAF418}\"," +
            "\"providerName\":\"PrinterProtocolProvider.dll\"}";

       printer = await PosPrinter.FromIdAsync(oobBlobBTPrinter);
```

## Related topics
[**Windows.Devices.PointOfService**](https://msdn.microsoft.com/library/windows/apps/dn298071)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20Out-of-band%20pairing%20%20RELEASE:%20%289/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


