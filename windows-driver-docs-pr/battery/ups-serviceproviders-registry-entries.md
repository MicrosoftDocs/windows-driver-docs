---
title: UPS ServiceProviders Registry Entries
description: Create a vendor-specific subkey under the UPS ServiceProviders registry key for each UPS model.
ms.assetid: fa206f16-e136-4bfe-9823-7c324d62e1fb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UPS\\ServiceProviders Registry Entries


## <span id="ddk_ups_serviceproviders_registry_entries_kg"></span><span id="DDK_UPS_SERVICEPROVIDERS_REGISTRY_ENTRIES_KG"></span>


Under the **UPS**\\**ServiceProviders** registry key, a UPS vendor should create a vendor-specific subkey. Under this subkey, the vendor should create an entry for each UPS model. Vendors must create these registry entries while [installing UPS minidrivers](installing-ups-minidrivers.md).

Each model-specific entry consists of a value name and a value. The value name should be the name of the UPS model. The value associated with this name is a string consisting of two parts:

-   The first part of the value string represents a hexadecimal bitmask identifying the model's capabilities. Bit values are defined in the following table.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Bit Value</th>
    <th align="left">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>0x00000001</p></td>
    <td align="left"><p>The UPS is installed.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>0x00000002</p></td>
    <td align="left"><p>The UPS supports power failure notification.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>0x00000004</p></td>
    <td align="left"><p>The UPS supports notification of low battery power.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>0x00000008</p></td>
    <td align="left"><p>The UPS can be turned off using the serial port.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>0x00000010</p></td>
    <td align="left"><p>Power failure notification is indicated by a positive signal.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>0x00000020</p></td>
    <td align="left"><p>Low battery notification is indicated by a positive signal.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>0x00000040</p></td>
    <td align="left"><p>The UPS is turned off by a positive signal.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>0x00000080</p></td>
    <td align="left"><p>Reserved. Do not use.</p></td>
    </tr>
    </tbody>
    </table>

     

-   The second part of the string is optional. It represents the path and name of the UPS minidriver. If this path and name is supplied, it must be preceded by a semicolon (;). If only the name is supplied, a default path of %SystemRoot%\\system32 is used.

After a UPS minidriver has been installed, and after a system administrator has enabled the UPS using **Power Options**, the system's UPS service copies model-specific **UPS**\\**ServiceProviders** values to other, system-controlled registry locations.

The following is an example of one vendor subkey, with value names and values for two UPS models, under **UPS**\\**ServiceProviders**:

``` syntax
UPS\ServiceProviders
    American Power Conversion
        Back-UPS "0x7f"
        Smart-UPS "0x1;apcups.dll"
```

 

 




