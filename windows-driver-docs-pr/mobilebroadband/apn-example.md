---
title: APN Example
description: APN example
ms.date: 04/20/2017
---

# APN example


The following XML document uses the [APN XML schema](apn-schema-definition.md) to specify the APN information for a service:

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<OperatorList 
  <Operator name="Contoso">
    <HardwareIdList>
      <HardwareId id="MBAE:0:XSDR^EREDER^F">
      </HardwareId>
    </HardwareIdList>
    <ConnectionInfoList>
      <ConnectionInfo AccessString="ContosoAPN" Username="user" Password="pass" FriendlyName="Prepaid Contoso Mobile Broadband" Internet="Y" Purchase="N" AutoConnectOrder="1"/>
    </ConnectionInfoList>
  </Operator>
</OperatorList>
```

 

 





