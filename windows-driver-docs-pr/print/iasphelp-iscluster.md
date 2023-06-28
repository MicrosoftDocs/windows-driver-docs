---
title: Iasphelp get_IsCluster method
description: The IsCluster property enables an ASP Web page to determine whether the Cluster service is running on a cluster node.
MS-HAID:
- 'webfnc_96d39d88-6d6f-49af-93d7-0f6668af9564.xml'
- 'print.iasphelp_iscluster'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_IsCluster method Print Devices", "get_IsCluster method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IsCluster method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_IsCluster
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_IsCluster method

The **IsCluster** property enables an ASP Web page to determine whether the Cluster service is running on a cluster node.

## Syntax

```cpp
HRESULT get_IsCluster(
  [out] BOOL *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives **TRUE** if the Cluster service is installed, configured, and running on the node, and **FALSE** otherwise.

## Return value

This property always returns S_OK.

## VBScript Example

This method calls the **GetNodeClusterState** function to determine the status of the Cluster service.

```vb
Dim objPrinter, ClusterRunning
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
ClusterRunning = objPrinter.IsCluster
```

## Requirements

**Target platform:** Desktop
