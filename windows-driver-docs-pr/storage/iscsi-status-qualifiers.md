---
title: ISCSI\_STATUS\_QUALIFIERS
description: ISCSI\_STATUS\_QUALIFIERS
ms.assetid: d39ed448-5608-4f19-b49c-bbd6727e9491
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_STATUS\_QUALIFIERS


## <span id="ddk_iscsi_status_qualifiers_kr"></span><span id="DDK_ISCSI_STATUS_QUALIFIERS_KR"></span>


The ISCSI\_STATUS\_QUALIFIERS WMI property qualifier corresponds to status values that are reported by a miniport driver that manages an iSCSI HBA initiator. These values are constructed by combining a severity code with a facility code and a facility status code that is described in *Ntstatus.h*.

The following table describes the ISCSI\_STATUS\_QUALIFIERS values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>Success.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_NON_SPECIFIC_ERROR (0xEFFF0001)</p></td>
<td align="left"><p>Nonspecific error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_LOGIN_FAILED (0xEFFF0002)</p></td>
<td align="left"><p>The logon failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_CONNECTION_FAILED (0xEFFF0003)</p></td>
<td align="left"><p>The connection failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INITIATOR_NODE_ALREADY_EXISTS (0xEFFF0004)</p></td>
<td align="left"><p>The initiator node already exists.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INITIATOR_NODE_NOT_FOUND (0xEFFF0005)</p></td>
<td align="left"><p>The initiator node does not exist.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_MOVED_TEMPORARILY (0xEFFF0006)</p></td>
<td align="left"><p>The target moved temporarily.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_TARGET_MOVED_PERMANENTLY (0xEFFF0007)</p></td>
<td align="left"><p>The target moved permanently.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INITIATOR_ERROR (0xEFFF0008)</p></td>
<td align="left"><p>Initiator error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_AUTHENTICATION_FAILURE (0xEFFF0009)</p></td>
<td align="left"><p>Authentication failure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_AUTHORIZATION_FAILURE (0xEFFF000A)</p></td>
<td align="left"><p>Authorization failure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_NOT_FOUND (0xEFFF000B)</p></td>
<td align="left"><p>Target not found.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_REMOVED (0xEFFF000C)</p></td>
<td align="left"><p>The target is removed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_UNSUPPORTED_VERSION (0xEFFF000D)</p></td>
<td align="left"><p>Unsupported version.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TOO_MANY_CONNECTIONS (0xEFFF000E)</p></td>
<td align="left"><p>Too many connections.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_MISSING_PARAMETER (0xEFFF000F)</p></td>
<td align="left"><p>Missing parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_CANT_INCLUDE_IN_SESSION (0xEFFF0010)</p></td>
<td align="left"><p>Cannot include connection in the session.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_SESSION_TYPE_NOT_SUPPORTED (0xEFFF0011)</p></td>
<td align="left"><p>The session type is not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_ERROR (0xEFFF0012)</p></td>
<td align="left"><p>Target error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_SERVICE_UNAVAILABLE (0xEFFF0013)</p></td>
<td align="left"><p>Service is unavailable.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_OUT_OF_RESOURCES (0xEFFF0014)</p></td>
<td align="left"><p>Out of resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_CONNECTION_ALREADY_EXISTS (0xEFFF0015)</p></td>
<td align="left"><p>Connections already exist on the initiator node.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_SESSION_ALREADY_EXISTS (0xEFFF0016)</p></td>
<td align="left"><p>The session already exists.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INITIATOR_INSTANCE_NOT_FOUND (0xEFFF0017)</p></td>
<td align="left"><p>The initiator instance does not exist.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_ALREADY_EXISTS (0xEFFF0018)</p></td>
<td align="left"><p>The target already exists.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_DRIVER_BUG (0xEFFF0019)</p></td>
<td align="left"><p>The iSCSI driver implementation did not complete an operation correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_TEXT_KEY (0xEFFF001A)</p></td>
<td align="left"><p>An invalid key text was encountered.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_SENDTARGETS_TEXT (0xEFFF001B)</p></td>
<td align="left"><p>An invalid endTargets response text was encountered.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_SESSION_ID (0xEFFF001C)</p></td>
<td align="left"><p>Invalid session identifier (ID).</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_SCSI_REQUEST_FAILED (0xEFFF001D)</p></td>
<td align="left"><p>The SCSI request failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TOO_MANY_SESSIONS (0xEFFF001E)</p></td>
<td align="left"><p>Exceeded maximum sessions for this initiator.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_SESSION_BUSY (0xEFFF001F)</p></td>
<td align="left"><p>The session is busy because a request is already in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_MAPPING_UNAVAILABLE (0xEFFF0020)</p></td>
<td align="left"><p>The target mapping is not available.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_ADDRESS_TYPE_NOT_SUPPORTED (0xEFFF0021)</p></td>
<td align="left"><p>The target address type is not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_LOGON_FAILED (0xEFFF0022)</p></td>
<td align="left"><p>The logon failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_SEND_FAILED (0xEFFF0023)</p></td>
<td align="left"><p>The TCP send failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TRANSPORT_ERROR (0xEFFF0024)</p></td>
<td align="left"><p>TCP transport error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_VERSION_MISMATCH (0xEFFF0025)</p></td>
<td align="left"><p>iSCSI version mismatch.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_MAPPING_OUT_OF_RANGE (0xEFFF0026)</p></td>
<td align="left"><p>The Target Mapping Address that is passed is out of range for the adapter configuration.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_TARGET_PRESHAREDKEY_UNAVAILABLE (0xEFFF0027)</p></td>
<td align="left"><p>The preshared key for the target or internet key exchange (IKE) identification payload is not available.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_AUTHINFO_UNAVAILABLE (0xEFFF0028)</p></td>
<td align="left"><p>The authentication information for the target is not available.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_TARGET_NOT_FOUND (0xEFFF0029)</p></td>
<td align="left"><p>The target name is not found or is marked as hidden from logon.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_LOGIN_USER_INFO_BAD (0xEFFF002A)</p></td>
<td align="left"><p>One or more parameters that are specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561600" data-raw-source="[&lt;strong&gt;LoginToTarget_IN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561600)"><strong>LoginToTarget_IN</strong></a> structure are invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_TARGET_MAPPING_EXISTS (0xEFFF002B)</p></td>
<td align="left"><p>The given target mapping already exists.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_HBA_SECURITY_CACHE_FULL (0xEFFF002C)</p></td>
<td align="left"><p>The HBA security information cache is full.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_PORT_NUMBER (0xEFFF002D)</p></td>
<td align="left"><p>The port number that is passed is not valid for the initiator.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_OPERATION_NOT_ALL_SUCCESS (0xEFFF002E)</p></td>
<td align="left"><p>The operation was not successful for all initiators.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_HBA_SECURITY_CACHE_NOT_SUPPORTED (0xEFFF002F)</p></td>
<td align="left"><p>The adapter does not have a security information cache.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_IKE_ID_PAYLOAD_TYPE_NOT_SUPPORTED (0xEFFF0030)</p></td>
<td align="left"><p>The IKE ID payload type that is specified is not supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_IKE_ID_PAYLOAD_INCORRECT_SIZE (0xEFFF0031)</p></td>
<td align="left"><p>The IKE ID payload size that is specified is not correct.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_PORTAL_ALREADY_EXISTS (0xEFFF0032)</p></td>
<td align="left"><p>The target portal structure already exists.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_TARGET_ADDRESS_ALREADY_EXISTS (0xEFFF0033)</p></td>
<td align="left"><p>The target address structure already exists.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_NO_AUTH_INFO_AVAILABLE (0xEFFF0034)</p></td>
<td align="left"><p>There is no IKE authentication information available.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_NO_TUNNEL_OUTER_MODE_ADDRESS (0xEFFF0035)</p></td>
<td align="left"><p>No tunnel mode outer address is specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_CACHE_CORRUPTED (0xEFFF0036)</p></td>
<td align="left"><p>The authentication or tunnel address cache is corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_REQUEST_NOT_SUPPORTED (0xEFFF0037)</p></td>
<td align="left"><p>The request or operation is not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_TARGET_OUT_OF_RESORCES (0xEFFF0038)</p></td>
<td align="left"><p>The target does not have enough resources to process the given request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_SERVICE_DID_NOT_RESPOND (0xEFFF0039)</p></td>
<td align="left"><p>The initiator service did not respond to the request that the driver sent.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_ISNS_SERVER_NOT_FOUND (0xEFFF003A)</p></td>
<td align="left"><p>The iSNS server was not found or is unavailable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_OPERATION_REQUIRES_REBOOT (0xAFFF003B)</p></td>
<td align="left"><p>The operation was successful but requires a driver reload or restart to become effective.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_NO_PORTAL_SPECIFIED (0xEFFF003C)</p></td>
<td align="left"><p>There is no target portal available to complete the logon.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_CANT_REMOVE_LAST_CONNECTION (0xEFFF003D)</p></td>
<td align="left"><p>The last connection for a session cannot be removed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_SERVICE_NOT_RUNNING (0xEFFF003E)</p></td>
<td align="left"><p>The iSCSI initiator service has not been started.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_TARGET_ALREADY_LOGGED_IN (0xEFFF003F)</p></td>
<td align="left"><p>The target has already been logged on through an iSCSI session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_DEVICE_BUSY_ON_SESSION (0xEFFF0040)</p></td>
<td align="left"><p>The session cannot be logged off because a device on that session is currently being used.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_COULD_NOT_SAVE_PERSISTENT_LOGIN_DATA (0xEFFF0041)</p></td>
<td align="left"><p>Failed to save persistent logon information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_COULD_NOT_REMOVE_PERSISTENT_LOGIN_DATA (0xEFFF0042)</p></td>
<td align="left"><p>Failed to remove persistent logon information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_PORTAL_NOT_FOUND (0xEFFF0043)</p></td>
<td align="left"><p>The specified initiator name was not found.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INITIATOR_NOT_FOUND (0xEFFF0044)</p></td>
<td align="left"><p>The specified portal was not found.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_DISCOVERY_MECHANISM_NOT_FOUND (0xEFFF0045)</p></td>
<td align="left"><p>The specified discovery mechanism was not found.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_IPSEC_NOT_SUPPORTED_ON_OS (0xEFFF0046)</p></td>
<td align="left"><p>iSCSI does not support the IPsec protocol for this version of the operating system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_PERSISTENT_LOGIN_TIMEOUT (0xEFFF0047)</p></td>
<td align="left"><p>The discovery service timed out waiting for all persistent logons to complete.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_SHORT_CHAP_SECRET (0xEFFF0048)</p></td>
<td align="left"><p>The specified CHAP secret is less than 96 bits and cannot be used for authentication negotiations over non-IPsec connections.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_EVALUATION_PEROID_EXPIRED (0xEFFF0049)</p></td>
<td align="left"><p>The evaluation period for the iSCSI discovery service has expired.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_CHAP_SECRET (0xEFFF004A)</p></td>
<td align="left"><p>The CHAP secret does not conform to the specification of the Challenge Handshake Authentication Protocol (CHAP) that the Network Working Group of the Internet Engineering Task Force (IETF) publishes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_TARGET_CHAP_SECRET (0xEFFF004B)</p></td>
<td align="left"><p>The target CHAP secret is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_INITIATOR_CHAP_SECRET (0xEFFF004C)</p></td>
<td align="left"><p>The initiator CHAP secret is invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_CHAP_USER_NAME (0xEFFF004D)</p></td>
<td align="left"><p>The CHAP user name is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_LOGON_AUTH_TYPE (0xEFFF004E)</p></td>
<td align="left"><p>The logon authentication type is invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_TARGET_MAPPING (0xEFFF004F)</p></td>
<td align="left"><p>The target mapping information is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_TARGET_ID (0xEFFF0050)</p></td>
<td align="left"><p>The 64-bit iSCSI target identifier in the target mapping is invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_ISCSI_NAME (0xEFFF0051)</p></td>
<td align="left"><p>The iSCSI name that is specified contains invalid characters or is too long.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INCOMPATIBLE_ISNS_VERSION (0xEFFF0052)</p></td>
<td align="left"><p>The iSNS version number that the iSNS server returned is not compatible with this version of the iSNS client.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_FAILED_TO_CONFIGURE_IPSEC (0xEFFF0053)</p></td>
<td align="left"><p>The initiator failed to configure IPSec for the given connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_BUFFER_TOO_SMALL (0xEFFF0054)</p></td>
<td align="left"><p>The buffer given for processing is too small.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_LOAD_BALANCE_POLICY (0xEFFF0055)</p></td>
<td align="left"><p>The given load balance policy is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_INVALID_PARAMETER (0xEFFF0056)</p></td>
<td align="left"><p>One or more parameters specified are invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_DUPLICATE_PATH_SPECIFIED (0xEFFF0057)</p></td>
<td align="left"><p>Duplicate path IDs were specified while attempting to set the load balance policy across redundant paths.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_PATH_COUNT_MISMATCH (0xEFFF0058)</p></td>
<td align="left"><p>Number of paths specified in setting the load balance policy does not match the number of paths available from the target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_PATH_ID (0xEFFF0059)</p></td>
<td align="left"><p>Path ID specified in setting the load balance policy is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_MULTIPLE_PRIMARY_PATHS_SPECIFIED (0xEFFF005A)</p></td>
<td align="left"><p>More than one primary path is specified when only one primary path is expected.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_NO_PRIMARY_PATH_SPECIFIED (0xEFFF005B)</p></td>
<td align="left"><p>No primary path specified when at least one is expected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_DEVICE_ALREADY_PERSISTENTLY_BOUND (0xEFFF005C)</p></td>
<td align="left"><p>Device is already a persistently bound device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_DEVICE_NOT_FOUND (0xEFFF005D)</p></td>
<td align="left"><p>Device was not found.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_DEVICE_NOT_ISCSI_OR_PERSISTENT (0xEFFF005E)</p></td>
<td align="left"><p>The device specified does not originate from an iSCSI disk or a persistent iSCSI login.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_DNS_NAME_UNRESOLVED (0xEFFF005F)</p></td>
<td align="left"><p>The DNS name specified was not resolved.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_NO_CONNECTION_AVAILABLE (0xEFFF0060)</p></td>
<td align="left"><p>There is no connection available in the iSCSI session to process the request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_LB_POLICY_NOT_SUPPORTED (0xEFFF0061)</p></td>
<td align="left"><p>The given Load Balance policy is not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_REMOVE_CONNECTION_IN_PROGRESS (0xEFFF0062)</p></td>
<td align="left"><p>A remove connection request is already in progress for this session.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_INVALID_CONNECTION_ID (0xEFFF0063)</p></td>
<td align="left"><p>Given connection was not found in the session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_CANNOT_REMOVE_LEADING_CONNECTION (0xEFFF0064)</p></td>
<td align="left"><p>The leading connection in the session cannot be removed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISDSC_RESTRICTED_BY_GROUP_POLICY (0xEFFF0065)</p></td>
<td align="left"><p>The operation cannot be performed because it does not conform with the group policy assigned to this computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ISDSC_ISNS_FIREWALL_BLOCKED (0xEFFF0066)</p></td>
<td align="left"><p>The operation cannot be performed because the Internet Storage Name Server (iSNS) firewall exception has not been enabled.</p></td>
</tr>
</tbody>
</table>

 

 

 





