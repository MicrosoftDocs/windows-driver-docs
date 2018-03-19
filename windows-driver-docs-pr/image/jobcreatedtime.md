---
title: JobCreatedTime element
description: The optional JobCreatedTime element specifies the time at which the job was created.
ms.assetid: 34107c3a-d02a-4b86-be1e-cd91e2887479
keywords: ["JobCreatedTime element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCreatedTime
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobCreatedTime element


The optional **JobCreatedTime** element specifies the time at which the job was created.

Usage
-----

``` syntax
<wscn:JobCreatedTime>
  text
</wscn:JobCreatedTime>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid value for the dateTime type. For more information about dateTime, see XML Schema Part 2: Datatypes Second Edition.**dateTimedateTime**

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A job is *created* when the job is submitted to the system.

The specified time refers to the internal clock of the scan device and does not need to be a real time clock.

## <span id="see_also"></span>See also


[**JobStatus**](jobstatus.md)

 

 






