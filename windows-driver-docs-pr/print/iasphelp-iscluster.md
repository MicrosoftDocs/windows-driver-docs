---
title: Iasphelp get\_IsCluster method
description: The IsCluster property enables an ASP Web page to determine whether the Cluster service is running on a cluster node.
MS-HAID:
- 'webfnc\_96d39d88-6d6f-49af-93d7-0f6668af9564.xml'
- 'print.iasphelp\_iscluster'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 78573fe7-d264-4d3c-8654-a85c2abfb93a
keywords: ["get_IsCluster method Print Devices", "get_IsCluster method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IsCluster method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_IsCluster
api_type:
- COM
---

# Iasphelp::get\_IsCluster method


The **IsCluster** property enables an ASP Web page to determine whether the Cluster service is running on a cluster node.

Syntax
------

```ManagedCPlusPlus
HRESULT get_IsCluster(
  [out] BOOL *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives **TRUE** if the Cluster service is installed, configured, and running on the node, and **FALSE** otherwise.

Return value
------------

This property always returns S\_OK.

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

This method calls the **GetNodeClusterState** function to determine the status of the Cluster service. For more information about this function, see the Windows SDK documentation.

```
    Dim objPrinter, ClusterRunning
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    ClusterRunning = objPrinter.IsCluster
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows XP and later versions of the Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_IsCluster%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




