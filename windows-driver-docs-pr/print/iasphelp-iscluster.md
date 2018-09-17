---
title: Iasphelp get\_IsCluster method
author: windows-driver-content
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
ms.localizationpriority: medium
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

 

 




