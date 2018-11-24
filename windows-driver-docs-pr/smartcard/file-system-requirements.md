---
title: File System Requirements
description: File System Requirements
ms.assetid: 2C363978-3C98-4838-8C55-F804D2C75BEC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Requirements


The “logical” layout is the data layout that was presented to the Base CSP/KSP. This layout uses more human-readable names, and the files may not correspond one-to-one with files in the physical layout that the card employs.

## <span id="File_Naming_Requirements"></span><span id="file_naming_requirements"></span><span id="FILE_NAMING_REQUIREMENTS"></span>File Naming Requirements


File names are composed of up to eight ANSI characters (8 bit), excluding characters that the Windows file and directory naming conventions do not allow. The directory structure consists of two levels: the root directory and directories that applications use. Directory names are composed of up to eight ANSI characters. To produce file names and directory names that are not case-sensitive, card minidriver implementations should convert strings to lowercase.

## <span id="File_Naming_Virtualization"></span><span id="file_naming_virtualization"></span><span id="FILE_NAMING_VIRTUALIZATION"></span>File Naming Virtualization


It is permissible to implement a virtual file system in the card minidriver that maps directories and files to appropriate locations on the card. Cards that do not allow write operations during normal operations (such as National ID cards) may simulate the writing operations but must maintain any files that are “written” for the duration of the insertion of the card and must be able to return these files when they are read.

## <span id="_Physical_Card_Data_Layout"></span><span id="_physical_card_data_layout"></span><span id="_PHYSICAL_CARD_DATA_LAYOUT"></span> Physical Card Data Layout


The following information about files on the card is an overview of how the card and file system are used. It is not intended that the card minidriver should be designed with knowledge of these files or their contents. The card minidriver should be written as a generalized interface layer.

## <span id="Logical_Data_Layout"></span><span id="logical_data_layout"></span><span id="LOGICAL_DATA_LAYOUT"></span>Logical Data Layout


### <span id="Card_Identifier"></span><span id="card_identifier"></span><span id="CARD_IDENTIFIER"></span>Card Identifier

The card identifier is a unique identifier for a card. It may be represented in some form to the user in the UI, but otherwise is used only for comparison to a reference value to establish the identity of a card. This value is assigned when the card is prepared for the user. It is organized as a byte array.

<span id="File_Name"></span><span id="file_name"></span><span id="FILE_NAME"></span>File Name  
The logical name for this file is “CardId”. It is in the root directory.

<span id="Access_Conditions"></span><span id="access_conditions"></span><span id="ACCESS_CONDITIONS"></span>Access Conditions  
The access conditions for this file are E(R), U(R), and A(RW).

<span id="Contents"></span><span id="contents"></span><span id="CONTENTS"></span>Contents  
The file is organized as a 16-byte array. It should be treated as opaque binary data.

<span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks  
This value is assigned by Microsoft software to assure that a unique value is generated for the card. It is unrelated to the serial number that may or may not be assigned to the card during manufacture.

### <span id="Application_Directory"></span><span id="application_directory"></span><span id="APPLICATION_DIRECTORY"></span>Application Directory

The Application directory file consists of a list of fixed-length application name entries. The application directory name is the name of the logical subdirectory that contains all of the application’s files. For an application that uses CAPI2, the name is “mscp”, for which the index value is zero.

<span id="Logical_Name"></span><span id="logical_name"></span><span id="LOGICAL_NAME"></span>Logical Name  
The logical name for this file is “cardapps”. It is in the root directory.

<span id="Access_Conditions"></span><span id="access_conditions"></span><span id="ACCESS_CONDITIONS"></span>Access Conditions  
The access conditions for this file are E(R), U(RW), and A(RW).

<span id="Contents"></span><span id="contents"></span><span id="CONTENTS"></span>Contents  
The file is organized as a series of records that contain a byte index followed by a zero-terminated application name string (ANSI).

<span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks  
The implementation of applications requires that application names map to a unique directory on the card and also to a unique index for the application’s data in the card cache file. The card application directory allows an application to find its index value in the cache file by finding its name in the application directory and noting the index of the position where this occurs. The file consists of an 8 byte records that contain the application name, zero filled at the end. The application name can use all 8 bytes so that there is no requirement that the resulting string be zero-terminated. Thus, the contents of the file for a “created” card are the following 8 bytes:

``` syntax
{‘mscp’,0,0,0,0}
```

### <span id="Cache_File"></span><span id="cache_file"></span><span id="CACHE_FILE"></span>Cache File

To improve performance and reduce communication with the card, the Base CSP/KSP can cache card data in various ways. The cache file is used to control operation of the caching subsystem within the Base CSP/KSP by indicating the version number of data on the card. When data is changed, this value is incremented. Comparing its internal copy of the cache file with the version that was read from the card allows the Base CSP/KSP to determine whether cached data can be used or must be refreshed. The need to make this determination can occur for many reasons, including withdrawing and reinserting the card.

Reading the card identifier and the cache file from the card should be entirely sufficient to permit using information that was cached for an indeterminate period of time on the host.

<span id="Logical_Name"></span><span id="logical_name"></span><span id="LOGICAL_NAME"></span>Logical Name  
The logical name for this file is “CardCF”. It is in the root directory.

<span id="Access_Conditions"></span><span id="access_conditions"></span><span id="ACCESS_CONDITIONS"></span>Access Conditions  
The access conditions for this file are E(R), U(RW), and A(RW).

<span id="Contents"></span><span id="contents"></span><span id="CONTENTS"></span>Contents  
The file is organized global data in the form of 2 byte values followed by a succession of 32-bit cache values that applications maintain and interpret. The first of these is reserved for the Base CSP/KSP to use. Thereafter, each application is allocated a single **DWORD**.

``` syntax
typedef struct _CARD_CACHE_FILE_FORMAT
{
    BYTE bVersion;          // Cache version
    BYTE bPinsFreshness;        // Card PIN
    WORD wContainersFreshness;
    WORD wFilesFreshness;

} CARD_CACHE_FILE_FORMAT, *PCARD_CACHE_FILE_FORMAT;
```

<span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks  
An application’s internal cache is refreshed if the cache data copy that is internal to the application indicates a different version number for the data of interest than the file read from the card. The cache is generally checked at the beginning of each transaction with the card.

The array of application cache data DWORDs, one for each caching application, is indexed by the application index from the application directory file. As applications are added, the file grows by 4-byte increments.

### <span id="Container_Map_File"></span><span id="container_map_file"></span><span id="CONTAINER_MAP_FILE"></span>Container Map File

The container map file is owned by the Base CSP/KSP and consists of a number of records of CONTAINERMAPRECORD type. These records associate a container identifier, which is typically a GUID that was assigned by CAPI to an index that can be used to access keys and certificates for that container.

The position (index) of the record in the file corresponds to the index of the certificate and key information that are associated with that container. Thus, the second record in such a file would see zero-based index 1.

The certificate that is associated with this container and the signing and/or key exchange keys for the container all share this index (UserCerts\\SignatureCert1, SignatureKey1, and so on). The records contain the container GUID and size information for keys that are associated with that index.

<span id="Logical_Name"></span><span id="logical_name"></span><span id="LOGICAL_NAME"></span>Logical Name  
The logical name for this file is “CMapFile”. It is in the “mscp” directory.

<span id="Access_Conditions"></span><span id="access_conditions"></span><span id="ACCESS_CONDITIONS"></span>Access Conditions  
The access conditions for this file are E(R), U(RW), and A(RW).

<span id="Contents"></span><span id="contents"></span><span id="CONTENTS"></span>Contents  
The access conditions for this file are E(R), U(RW), and A(RW).

<span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks  
This file is created and its content maintained by the Base CSP/KSP. Information about the internal structure of this file is provided for reference only. The records in the file have the following format:

**CONTAINERMAPRECORD**

These records contain the CAPI-assigned container GUID and the key sizes for the associated key exchange or signing keys that are associated with that container. All WORD members are little-Endean byte order.

``` syntax
//
// Type: CONTAINER_MAP_RECORD
//
// This structure describes the format of the Base CSP's 
// container map file, stored on the card. This is well-known 
// logical file wszCONTAINER_MAP_FILE. The file consists of 
// zero or more of these records.
//
#define MAX_CONTAINER_NAME_LEN                  39

// This flag is set in the CONTAINER_MAP_RECORD bFlags 
// member if the corresponding container is valid and currently 
// exists on the card. // If the container is deleted, its 
// bFlags field must be cleared.
#define CONTAINER_MAP_VALID_CONTAINER           1

// This flag is set in the CONTAINER_MAP_RECORD bFlags
// member if the corresponding container is the default
// container on the card.
define CONTAINER_MAP_DEFAULT_CONTAINER         2

typedef struct _CONTAINER_MAP_RECORD
{
    WCHAR wszGuid [MAX_CONTAINER_NAME_LEN + 1];
    BYTE bFlags;
    BYTE bReserved;
    WORD wSigKeySizeBits;
    WORD wKeyExchangeKeySizeBits;
} CONTAINER_MAP_RECORD, *PCONTAINER_MAP_RECORD;
```

The **wszGuid** member consists of a UNICODE character string representation of an identifier that CAPI assigned to the container. This is usually, but not always, a GUID string. Identifier names cannot contain the special character “\\”. When read-only cards are provisioned, the provisioning process must follow the same guidelines for identifier names.

Container names must be null-terminated and must not be greater than (MAX\_CONTAINER\_NAME\_LEN + 1) characters in length including the NULL terminator.

If a record must be removed from this table, the entry is invalidated by writing zeroes to the record. Such a record can later be overwritten by new data. The table is not “packed” to remove inactive entries.

The following bits are valid for the Flags byte:

-   Bit 0 is set when the container record is valid.
-   Bit 1 is set when the container is default. Only one record in the container map can have this bit set at any time. This bit can be set only if Bit 0 is also set. In other words, you cannot have a default container that is not valid. All other bits are currently reserved for future revisions of the card minidriver.
-   For the default container, this translates to the byte 0x03. For a valid container that is not the default, this value is 0x01.
-   Bits 2-7 are reserved for future use.

## <span id="Data_Layout_Summary"></span><span id="data_layout_summary"></span><span id="DATA_LAYOUT_SUMMARY"></span>Data Layout Summary


The following table summarizes the organization of the data at the interface between the card minidriver and the Base CSP/KSP for a typical implementation. The “Logical Name” is the string that the Base CSP/KSP uses to communicate with the card minidriver; it may or may not directly map to a corresponding element on the card.

Note that certificates and keys are logically grouped by the Base CSP/KSP into subdirectories according to their purpose, by using only an index for the actual file name. Any certificates or keys that are added to the card are named according to their index number in their directory. Some example certificates and keys are shown in the following table for the purpose of illustration.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Directory name</th>
<th align="left">File name</th>
<th align="left">Type</th>
<th align="left">Access conditions</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">&lt;root&gt;</td>
<td align="left">cardid</td>
<td align="left">File</td>
<td align="left">E(R) U(R) A(RW)</td>
<td align="left">Card identifier</td>
</tr>
<tr class="even">
<td align="left">&lt;root&gt;</td>
<td align="left">cardcf</td>
<td align="left">File</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">Cache file</td>
</tr>
<tr class="odd">
<td align="left">&lt;root&gt;</td>
<td align="left">cardapps</td>
<td align="left">File</td>
<td align="left">E(R) U(R) A(RW)</td>
<td align="left"><p>Directory index by application name.</p>
<p>For more information, see &#39;Application Directory&#39;.</p></td>
</tr>
<tr class="even">
<td align="left">mscp</td>
<td align="left"></td>
<td align="left">Dir</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">Base CSP/KSP App Directory</td>
</tr>
<tr class="odd">
<td align="left">mscp</td>
<td align="left">cmapfile</td>
<td align="left">File</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">CAPI GUID to index</td>
</tr>
<tr class="even">
<td align="left">mscp</td>
<td align="left">kxc00</td>
<td align="left">File</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">(example) key exchange cert 0</td>
</tr>
<tr class="odd">
<td align="left">mscp</td>
<td align="left">ksc00</td>
<td align="left">File</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">(example) key signature cert 0</td>
</tr>
<tr class="even">
<td align="left">mscp</td>
<td align="left">ksc01</td>
<td align="left">File</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">(example) key signature cert 1</td>
</tr>
<tr class="odd">
<td align="left">mscp</td>
<td align="left">msroots</td>
<td align="left">File</td>
<td align="left">E(R) U(RW) A(RW)</td>
<td align="left">Enterprise trusted roots</td>
</tr>
</tbody>
</table>

 

**Note**  Interoperability with msroots: mscp\\msroots file is a PKCS \#7 formatted certificate store.

 

## <span id="File_Access_Control"></span><span id="file_access_control"></span><span id="FILE_ACCESS_CONTROL"></span>File Access Control


### <span id="Known_Principals"></span><span id="known_principals"></span><span id="KNOWN_PRINCIPALS"></span>Known Principals

Known principals are identifiers for the various types of users that can attempt to access card data in some way. The following table shows valid principals, with a single letter abbreviation that can be used together with a data access operation identifier to define an access condition. Although there can be more identifiable principals, the listing is restricted to those that have meaning to the communication between the Base CSP/KSP and the card minidriver.

| Name          | Description                                                                                                                                                                                                                                                                                 | Mnemonic | PIN\_ID mapping    |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------|
| Everyone      | Any requestor, including unauthenticated (or anonymous) users.                                                                                                                                                                                                                              | E        | ROLE\_EVERYONE (0) |
| User          | A user client of the card, who proves his identity to the card by use of a PIN.                                                                                                                                                                                                             | U        | ROLE\_USER (1)     |
| Administrator | Card issuer or other party with an administrative relationship to the card or data on the card. Uses a special PIN or KEY (that may or may not be unique to the card or user) to perform administrative tasks that the user cannot perform without using this data, such as PIN unblocking. | A        | ROLE\_ADMIN (2)    |

 

When “everyone” is used in the following discussion, it typically means any user of the card, whether authenticated or not. “Everyone can read a file,” for example, means that the user or administrator can automatically read the file.

For file system access, the administrator is generally regarded as a “super-user” and has all the same privileges as the user (with the exception of execute privilege).

### <span id="Directory_Access_Conditions"></span><span id="directory_access_conditions"></span><span id="DIRECTORY_ACCESS_CONDITIONS"></span>Directory Access Conditions

Principals can create directories in the card file system with two sets of permissions. The following table summarizes the effect of each of the permissions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Directory access condition</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">UserCreateDeleteDirAc</td>
<td align="left"><p>The user and administrator can create files in the directory by using <a href="https://msdn.microsoft.com/library/windows/hardware/dn468711" data-raw-source="[&lt;strong&gt;CardCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468711)"><strong>CardCreateFile</strong></a>.</p>
<p>The user and administrator can delete the Directory (if it is not empty) by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn468716" data-raw-source="[&lt;strong&gt;CardDeleteDirectory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468716)"><strong>CardDeleteDirectory</strong></a>.</p>
<p>Everyone can list the contents of the directory by using <a href="https://msdn.microsoft.com/library/windows/hardware/dn468721" data-raw-source="[&lt;strong&gt;CardEnumFiles&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468721)"><strong>CardEnumFiles</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left">AdminCreateDeleteDirAc</td>
<td align="left"><p>The administrator can create files in the directory by using <a href="https://msdn.microsoft.com/library/windows/hardware/dn468711" data-raw-source="[&lt;strong&gt;CardCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468711)"><strong>CardCreateFile</strong></a>.</p>
<p>The administrator can delete the Directory by using <a href="https://msdn.microsoft.com/library/windows/hardware/dn468716" data-raw-source="[&lt;strong&gt;CardDeleteDirectory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468716)"><strong>CardDeleteDirectory</strong></a>.</p>
<p>Everyone can list the contents of the directory by using <a href="https://msdn.microsoft.com/library/windows/hardware/dn468721" data-raw-source="[&lt;strong&gt;CardEnumFiles&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468721)"><strong>CardEnumFiles</strong></a>.</p>
<div class="alert">
<strong>Note</strong>  This ACL is optional. It may be removed from future revisions of the smart card minidriver specification.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

**Note**  When creating a directory, everyone automatically has permissions to list the files in the directory. There are no separate “list” permissions for directories.

 

### <span id="File_Access_Operations"></span><span id="file_access_operations"></span><span id="FILE_ACCESS_OPERATIONS"></span>File Access Operations

Principals can use the contents of files in various ways. Valid operations are listed in the following table, with a single letter abbreviation that can be used, together with a principal designator to define an access condition. In particular, note that Execute (X) has no logical relationship to other file access operations—it is an independent operation.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operations/privileges</th>
<th align="left">Description</th>
<th align="left">Mnemonic</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Read</td>
<td align="left"><p>Receive the contents of the file either directly or in a formatted or processed form.</p></td>
<td align="left">R</td>
</tr>
<tr class="even">
<td align="left">Write</td>
<td align="left"><p>Change the contents of a file, possibly creating the file, or removing, replacing, or altering existing data.</p></td>
<td align="left">W</td>
</tr>
<tr class="odd">
<td align="left">Execute</td>
<td align="left"><p>Use the file contents for an operation that is conducted by the card on the requestor’s behalf, without being able to receive the data so used or feasibly derive it.</p></td>
<td align="left">X</td>
</tr>
</tbody>
</table>

 

### <span id="_File_Access_Conditions"></span><span id="_file_access_conditions"></span><span id="_FILE_ACCESS_CONDITIONS"></span> File Access Conditions

Access conditions are similar to ACLs. Access conditions control which principals can access a given file and what operations they can perform. Each file on the card has an access condition that can be described by a list of principals and their access privileges. If a principal or a privilege is not included in a description, it is assumed to be denied. Generally speaking, access conditions are enforced on the card.

The following table lists the access conditions that are available through [**CardCreateFile**](https://msdn.microsoft.com/library/windows/hardware/dn468711) and maps them to the appropriate access condition mnemonic.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">File access condition</th>
<th align="left">Actual meaning</th>
<th align="left">Access condition mnemonic</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">InvalidAc</td>
<td align="left"><p>There was an error retrieving the ACL.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">EveryoneReadUserWriteAc</td>
<td align="left"><p>This means that everyone can read the file or get the file information (<a href="https://msdn.microsoft.com/library/windows/hardware/dn468727" data-raw-source="[&lt;strong&gt;CardReadFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468727)"><strong>CardReadFile</strong></a> or <strong>CardGetFileInfo</strong>), respectively, and that the user and administrator can read the file, write the file, and delete the file.</p></td>
<td align="left">E(R), U(RW), A(RW)</td>
</tr>
<tr class="odd">
<td align="left">UserWriteExecuteAc</td>
<td align="left"><p>The user can write the file, can “execute” the file, and can delete the file. No one, including the user, can read the contents of the file. The administrator can also write, but not execute, the contents of this file and can delete the file.</p></td>
<td align="left">U(WX) A(W)</td>
</tr>
<tr class="even">
<td align="left">EveryoneReadAdminWriteAc</td>
<td align="left"><p>This means that everyone can read the file or get the file information (<a href="https://msdn.microsoft.com/library/windows/hardware/dn468727" data-raw-source="[&lt;strong&gt;CardReadFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn468727)"><strong>CardReadFile</strong></a> or <strong>CardGetFileInfo</strong>), respectively, but that only the administrator can write the file and delete the file.</p></td>
<td align="left">E(R), U(R), A(RW)</td>
</tr>
<tr class="odd">
<td align="left">UnknownAc</td>
<td align="left"><p>The file is protected by an access condition (AC) on the card that is not one of the predefined AC types.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">UserReadWriteAc</td>
<td align="left"><p>Everyone No Access // User Read Write // // Example: A password wallet file</p></td>
<td align="left">U(RW), A(RW)</td>
</tr>
<tr class="odd">
<td align="left">AdminReadWriteAc</td>
<td align="left"><p>Everyone/User No Access</p>
<p>// Admin Read Write</p>
<p>//</p>
<p>// Example: Administration data.</p></td>
<td align="left">A(RW)</td>
</tr>
</tbody>
</table>

 

The following table lists some sample access conditions for common items.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Access condition</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">E(X) U(W) A(W)</td>
<td align="left"><p>This would be the access condition for the user PIN. A user is unidentified when an operation that requires the PIN begins. The PIN must be “executed” to establish the user’s identity. After entry of the PIN, the user’s identity is promoted from E to U. Both the user and the administrator may write a PIN.</p></td>
</tr>
<tr class="even">
<td align="left">U(WX) A(W)</td>
<td align="left"><p>The user’s private key file may never be read from the card, and only the user may use its contents for cryptographic operations. This data may be changed by either the user or administrator.</p></td>
</tr>
<tr class="odd">
<td align="left">E(R) U(R) A(RW)</td>
<td align="left"><p>Card identifier.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Notes_on_the_Directory_and_File_Access_Conditions"></span><span id="notes_on_the_directory_and_file_access_conditions"></span><span id="NOTES_ON_THE_DIRECTORY_AND_FILE_ACCESS_CONDITIONS"></span>Notes on the Directory and File Access Conditions

-   The principal needs Read access on the file for [**CardGetFileInfo**](https://msdn.microsoft.com/library/windows/hardware/dn468727) to succeed.
-   There are no separate list permissions for listing the contents of a directory.
-   “Create access on a directory” means having the privilege to create files in the directory, whereas “delete access on the directory” means having the privilege to delete the directory itself. To delete a file, the card principal must have write access to the file itself.
-   It is not possible through the smart card minidriver interface to create directories with E(W) permissions.
-   It is not possible through the smart card minidriver interface to change file or directory permissions without deleting and re-creating the file or directory.
-   It is not possible through the smart card minidriver interface to create a private key file that is owned by either the administrator or by a non-authenticated user.
-   It is not possible through the smart card minidriver interface to create a PIN file on the card (E(X), U(W), and A(W)).
-   It is not possible through the smart card minidriver interface to query directory access conditions.
-   It is only possible through the smart card minidriver interface to create files with a subset of the access condition combinations that are available.

 

 





