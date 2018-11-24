---
title: ConnectionInfo
description: ConnectionInfo
ms.assetid: bbdba286-4d28-46b6-bafa-83cbddd883ae
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ConnectionInfo


The ConnectionInfo element specifies a list of connections for the specified operator.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ConnectionInfoList AccessString=”xs:string” Username=”xs:string” Password=”xs:string” FriendlyName=”xs:string” Purchase=”xs:Boolean” Internet=”xs:Boolean” AutoConnectOrder=”xs:positiveinteger” Compression=”xs:token” AutoProtocol=”xs:token”>
</ConnectionInfoList>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AccessString</p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p>The name and country/region of the operator.</p>
<p>Example: Contoso (Argentina)</p></td>
</tr>
<tr class="even">
<td><p>Username</p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p>The username is used to connect to the Internet.</p></td>
</tr>
<tr class="odd">
<td><p>Password</p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p>The password used to connect to the Internet.</p></td>
</tr>
<tr class="even">
<td><p>FriendlyName</p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p>The value shown in Windows Connection Manager in the APN drop-down box.</p></td>
</tr>
<tr class="odd">
<td><p>Purchase</p></td>
<td><p>xs:boolean</p></td>
<td><p>Yes</p></td>
<td><p>Denotes whether the access string should be used for purchase or Internet.</p></td>
</tr>
<tr class="even">
<td><p>Internet</p></td>
<td><p>xs:boolean</p></td>
<td><p>Yes</p></td>
<td><p>Denotes whether the access string should be used for purchase or Internet.</p></td>
</tr>
<tr class="odd">
<td><p>AutoConnectOrder</p></td>
<td><p>xs:positiveinteger</p></td>
<td><p>No</p></td>
<td><p>Determines the order in which Windows tries to connect to each of the APNs in the <a href="connectioninfolist.md" data-raw-source="[ConnectionInfoList](connectioninfolist.md)">ConnectionInfoList</a> element.</p></td>
</tr>
<tr class="even">
<td><p>Compression</p></td>
<td><p>xs:token</p></td>
<td><p>No</p></td>
<td><p>Specifies if compression will be used at the data link for header and data transfer.</p>
<p>Values: ENABLE or DISABLE</p></td>
</tr>
<tr class="odd">
<td><p>AuthProtocol</p></td>
<td><p>xs:token</p></td>
<td><p>No</p></td>
<td><p>Specifies the authentication protocol used for activating a PDP context.</p>
<p>Values: NONE, PAP, CHAP, or MsCHAPv2</p></td>
</tr>
</tbody>
</table>

 

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


There are no child elements.

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="connectioninfolist.md" data-raw-source="[ConnectionInfoList](connectioninfolist.md)">ConnectionInfoList</a></p></td>
<td><p>Specifies the details for an operator in the APN database.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element ref="ConnectionInfo" maxOccurs="unbounded"/>

<xs:element name="ConnectionInfo">
  <xs:complexType>
    <xs:attribute name="AccessString" use="optional">
      <!--The AccessString element identifies the APN or dial string to be used to establish a data connection -->
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:minLength value="0"/>
          <xs:maxLength value="100"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Username" use="optional">
      <!--The UserName element specifies the user name for logon -->
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:minLength value="0"/>
          <xs:maxLength value="255"/>
          <xs:whiteSpace value="collapse"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Password" use="optional">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:minLength value="0"/>
          <xs:maxLength value="255"/>
          <xs:whiteSpace value="collapse"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="FriendlyName" use="optional">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:minLength value="0"/>
          <xs:maxLength value="255"/>
          <xs:whiteSpace value="collapse"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Purchase" type="xs:boolean" use="required"/>
    <xs:attribute name="Internet" type="xs:boolean" use="required"/>
    <xs:attribute name="AutoConnectOrder" type="xs:positiveInteger" use="optional"/>
    <xs:attribute name="Compression" use="optional">
      <xs:simpleType>
        <xs:restriction base="xs:token">
          <xs:enumeration value="DISABLE"/>
          <xs:enumeration value="ENABLE"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="AuthProtocol" use="optional">
      <xs:simpleType>
        <xs:restriction base="xs:token">
          <xs:enumeration value="NONE"/>
          <xs:enumeration value="PAP"/>
          <xs:enumeration value="CHAP"/>
          <xs:enumeration value="MsCHAPv2"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
</xs:element>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ConnectionInfo element is required.

 

 





