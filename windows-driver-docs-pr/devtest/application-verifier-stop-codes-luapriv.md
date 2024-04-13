---
title: Application Verifier - Stop Codes - LuaPriv
description: Application Verifier - Stop Codes - LuaPriv
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/14/2022
---

# Application Verifier - Stop Codes - LuaPriv

The following stop codes are contained in this set of tests.

<h3>The Verifier could not get an object's name.</h3>
<p></p><i>Probable cause</i><p>The Verifier attempted to canonicalize the name of an object opened by the application, but was unable to do so. This indicates that some diagnostic information may be missing from reports of security issues.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Object: Unable to query the object's name 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle to the Object</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;NTSTATUS</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Key Type</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Key Data</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANNOTQUERYOBJECT</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not get an object's path name.</h3>
<p></p><i>Probable cause</i><p>The Verifier could not find the canonical path to the object. As a result, the object's name will probably be incomplete. This may make it difficult to locate the source of any problems the Predictor does find.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Object: Could not get '%hs' from pathname (%ws) due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Type of name (LPSTR)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Pathname (LPWSTR) </li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;LastError</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANTCANONICALIZEPATH</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not open an object.</h3>
<p></p><i>Probable cause</i><p>The Verifier tried unsuccessfully to open an object to obtain information from it. The object was not analyzed.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Object: Cannot open '%hs' (%ws) for '%hs' due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Description of the object (LPSTR)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Pathname (LPWSTR)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Parent handle (Registry only)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANTOPEN_NONCRITICAL</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Could not interpret HKEY_CURRENT_USER.</h3>
<p></p><i>Probable cause</i><p>The Verifier was unable to interpret HKEY_CURRENT_USER in the way it was listed. Without knowing the canonical path to HKCU, registry keys there may be inappropriately flagged as restrictive by the Verifier.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Registry: Could not '%hs' HKEY_CURRENT_USER due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Win32 ErrorKey Handle (if open)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Key Handle (if open)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;BADHKCU</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Initialization failed.</h3>
<p></p><i>Probable cause</i><p>The USERPROFILE environment variable could not be found. Because of this, the current user's profile could not be identified and opened; therefore, the Verifier might falsely identify some files and/or directories as being excessively restrictive.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Profile: The USERPROFILE environment variable could not be found</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;NO_USERPROFILE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Okay Object.</h3>
<p></p><i>Probable cause</i><p>The Verifier assumed that this object was inherently 'safe' due to its location.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs '%ws' looks okay because it exists in (%ws)</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Object Prefix</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Object Handle (if available)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;OK_OBJECT_PREFIX</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Object opened/created in a restricted namespace.</h3>
<p></p><i>Probable cause</i><p>This object was found in the listed namespace, which is not writable by standard users. Use the Local\ prefix for standard user account compliance.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs '%ws' is in restricted namespace (%ws)</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Namespace</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Object Handle (if available)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;RESTRICTED_NAMESPACE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Object opened/created without a namespace.</h3>
<p></p><i>Probable cause</i><p>This object was created without a namespace, which can cause it to be created in Session\ or Global\, depending on whether Terminal Server is used. Use the Local\ prefix for standard user account compliance. Note: In Windows Vista, the object will be created in the Local\ namespace.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs '%ws' has no namespace</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Object Handle (if available)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;NO_NAMESPACE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not find the parent directory.</h3>
<p></p><i>Probable cause</i><p>The Verifier attempted to determine where a file or directory resided, but an error prevented this.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: Could not canonicalize (%ws) due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;API Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Child Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANTGETPARENT</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not open an object's parent.</h3>
<p></p><i>Probable cause</i><p>The Verifier was unable to open the parent of the given object (to determine whether standard users would be able to create child objects). As a result, the parent has not been analyzed.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;File: Could not open '%hs' (%ws) to validate call to %hs '%ws' due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Parent Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Child Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Child Object Handle (if available)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANT_OPEN_PARENT</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application is running with privilege.</h3>
<p></p><i>Probable cause</i><p>The verifier discovered that the application was being run by an administrative user. This may be already known, but when intentionally running as a standard user, the user account should not be a member of the listed group.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Running as a user in privileged group '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privileged Group</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;NON_LUA_USER</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Sid conversion failed.</h3>
<p></p><i>Probable cause</i><p>The Verifier failed to convert a static (configuration) Security Identifier (SID) from the human-readable form to the form usable by Windows.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Failed to convert '%hs' to sid due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;String Sid</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;STRING2SID_FAILED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called the GetTokenInformation function.</h3>
<p></p><i>Probable cause</i><p>The application called the GetTokenInformation function and requested the listed class of information. This will work as a standard user, but it generally indicates that the application expects to be run by an administrator and is examining the access token to determine this.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Privs: Called GetTokenInformation, requesting '%hs'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Type Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Type </li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;GETTOKENINFO</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Cannot find the canonical name for a privilege.</h3>
<p></p><i>Probable cause</i><p>This privilege probably does not exist on your version of Windows. This break message is no cause for concern and is purely diagnostic information.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Could not determine displayname of '%ws' due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_PRIVILEGE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not look up the privilege.</h3>
<p></p><i>Probable cause</i><p>The Verifier was prevented from looking up the name of the privilege with the listed LUID. This will prevent the Verifier from producing certain diagnostics.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Could not determine name of privilege for '%hs' due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege LUID *</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Requesting API</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;PRIV_LOOKUP_FAILED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Requested a security-relevant privilege.</h3>
<p></p><i>Probable cause</i><p>The application requested (and received) the listed privilege, which is not granted to standard users. This API call will fail as a standard user account, which may have performance and audit implications in addition to having an impact on the functionality of the application.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Privs: Requested %ws%hs%ws%hs with %hs successfully</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege LUID *</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Privilege's display name (if available)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Requesting API</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;USED_PRIVILEGE_LUID</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application requested a security-relevant privilege.</h3>
<p></p><i>Probable cause</i><p>The application unsuccessfully requested the listed privilege, which is not granted to standard users. The API call will fail as a standard user, which may have performance and audit implications, in addition to having an impact on the application's functionality.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Privs: Requested %ws%hs%ws%hs with %hs, but was denied</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege LUID *</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Privilege's display name (if available)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Requesting API</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FAILED_PRIVILEGE_LUID</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application is running with privilege.</h3>
<p></p><i>Probable cause</i><p>The application was launched by a user with access to the listed privilege. This indicates that the user is not a standard user. This may already be known, but to run as a standard user, the user should NOT be granted the given listed privilege.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Running as user with access to %ws%hs%ws%hs</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege LUID *</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Privilege's display name (if available)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;PRIVILEGED_USER</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Failed to enable a non-security-relevant privilege.</h3>
<p></p><i>Probable cause</i><p>The application requested the listed privilege unsuccessfully. Although this privilege is not security-relevant (E.G. a standard user might have the privilege), this could be indicative of nonstandard privilege requirements in the application. In this case, the application may generate excessive audit traffic or its functionality may be impaired.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Privs: Could not enable '%ws' (the '%ws' privilege) with %hs</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege LUID *</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Privilege's name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Requesting API</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Privilege's displayname (if available)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;IRRELEVANT_PRIVILEGE_DENIED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application failed to enable a non-security relevant privilege.</h3>
<p></p><i>Probable cause</i><p>The application requested the listed privilege unsuccessfully. Although this privilege is not security-relevant (E.G. a standard user might potentially have the privilege), this could be indicative of nonstandard privilege requirements in the application. In this case, the application may generate excessive audit traffic or its functionality may be impaired.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Privs: Could not enable unknown privilege '%ws' with %hs</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Privilege LUID *</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Privilege's name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Requesting API</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Privilege's displayname (if available)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;IRRELEVANT_UNKNOWN_PRIVILEGE_DENIED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not query a registry value.</h3>
<p></p><i>Probable cause</i><p>The Verifier tried unsuccessfully to query a registry value.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Registry: Could not query value '%ws' due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Key Handle</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Value Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Win32 Error</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANT_QUERY_VALUE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The Verifier could not parse an INI file mapping.</h3>
<p></p><i>Probable cause</i><p>The application used an INI file that was mapped to a registry key by the system. While parsing the structure of that INI file mapping, the Verifier encountered unknown syntax. The API call has not been checked.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Ini: Did not understand the '%ws' in '%ws' -- unknown INI file mapping prefix</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Value Mapping</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;INI Mapping</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;N/A</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_MAPPING</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application was denied access to an object.</h3>
<p></p><i>Probable cause</i><p>The application was denied access to the given profile section due to insufficient privilege. If the application's functionality is imparied, this access problem may be the cause.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Ini: %hs Denied access to profile '%ws' due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;INI File (profile)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Section</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Win32 Error</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;INI_PROFILE_ACCESS_DENIED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application was able to access the object's security descriptor.</h3>
<p></p><i>Probable cause</i><p>The application was granted the requested access to this object. A standard user should also be able to access this object.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: (%ws) access 0x%x is okay '%hs'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Access Requested</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Security Descriptor</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;String Security Descriptor</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;OK_OBJECT_DUMP</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The object's security descriptor is inaccessible.</h3>
<p></p><i>Probable cause</i><p>The application was granted the requested access to this object. A standard user, however, may have trouble accessing this object.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: (%ws) access 0x%x granted to '%hs'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Access Requested</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Security Descriptor</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;String Security Descriptor</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;BAD_OBJECT_DUMP</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unable to display a security descriptor.</h3>
<p></p><i>Probable cause</i><p>The Verifier attempted to display a security descriptor, but could not render it into human-readable form. This is probably due to low memory, but could be the result of a non-standard security descriptor.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Could not convert %hs security descriptor '%ws' to text due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Security Descriptor</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Win32 Error</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;SD2TEXT</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Deny Access Control Entry (ACE) encountered.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) and requested access that was explicitly denied to one or more entities. Depending on who is denied access, this might prevent access by less-privileged users.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: (%ws) denies '%hs' to '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Control Entry</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Access Mask</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;DENY_ACE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Access was restricted to trusted users only.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) and requested access permissions that were granted solely to trusted users. This indicates that untrusted users will have difficulty running the application correctly.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) only grants requested '%hs' to '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Mask</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;String SID</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;RESTRICTED_RIGHT</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Access was restricted to trusted users only.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) and requested access permissions that were granted solely to trusted users. This indicates that untrusted users will have difficulty running the application correctly. This message will always be followed by other messages.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) only grants requested '%hs' to '%ws' (and others-- see subsequent stops)</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Mask</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;String SID</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;RESTRICTED_RIGHT_MORE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Access is restricted solely to the owner.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) and requested access that is granted to privileged entities AND TO THE OWNER. The owner is also currently privileged, suggesting that this object will not be accessible by unprivileged entities.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) grants '%hs' to 'Creator/Owner'.  The current owner is '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Mask</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;SID of the current owner</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CREATOR_OWNER</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Safe Object.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) and requested access that is granted to at least one non-privileged entity (listed). This suggests that the same operation will work when attempted by non-privileged/standard users.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: (%ws) looks okay because it grants to '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Control Entry</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;OK_OBJECT_GRANT</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Inaccessible object.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) that grants no explicit access to anyone. Barring administrative intervention (such as SE_TAKEOWNERSHIP_PRIVILEGE or SE_BACKUP_PRIVILEGE), the operation being performed by the application should never succeed. Therefore, what the application is doing will not work for standard users.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: (%ws) DACL allows no access by 'anyone'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Object's DACL</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;N/A</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;EMPTY_DACL</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Part of a security descriptor is missing.</h3>
<p></p><i>Probable cause</i><p>The Verifier attempted to analyze the object's security descriptor, but received an unexpected error when attempting to break it into pieces for scrutiny. This may suggest that the object's security descriptor could be invalid.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Object: Could not query %hs (%ws) %hs due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;What's Missing (string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Security Descriptor</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Win32 error</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;MISSING_PIECE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Part of a security descriptor is missing.</h3>
<p></p><i>Probable cause</i><p>The Verifier attempted to analyze the object's security descriptor, but received an unexpected error when attempting to break it into pieces for scrutiny. This may suggest that the object's security descriptor could be invalid.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Object: Could not retrieve ACE number %ld from %hs (%ws) DACL due to error 0x%x</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Missing ACE index</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Security Descriptor</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Win32 error</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;MISSING_ACE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application requested MAXIMUM_ALLOWED access.</h3>
<p></p><i>Probable cause</i><p>The application requested MAXIMUM_ALLOWED access to an object (such as a file or registry key). Because of this, the open function will always succeed, even if no permission is actually granted to the user. This is unacceptable programming practice. In addition, the Verifier cannot authoritatively determine what rights the application actually needs in order to operate. The Verifier has attempted to analyze the application as if all access privileges granted were actually required, which may cause false-positives.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: Opened (%ws) with '%hs' for 0x%x (%hsMAXIMUM_ALLOWED), was granted 0x%x access</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Requested Access</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Granted Access</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;MAXIMUM_ALLOWED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application requested MAXIMUM_ALLOWED access.</h3>
<p></p><i>Probable cause</i><p>The application requested MAXIMUM_ALLOWED access to an object (such as a file or registry key). Because of this, the open function will always succeed, even if no permission is actually granted to the user. This is unacceptable programming practice. In addition, the Verifier cannot authoritatively determine what rights the application actually needs in order to operate. The Verifier has attempted to determine what rights might have been granted to the application by the object, but failed to do so.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: Openned (%ws) with '%hs' for 0x%x (%hsMAXIMUM_ALLOWED), but granted access could not be determined due to error 0x%x.  The object should be checked manually</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Requested Access</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Error Value</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_MAXIMUM_ALLOWED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Skipped unknown permissions.</h3>
<p></p><i>Probable cause</i><p>The application requested permissions that are unknown to the Verifier. Lacking context, the Predictor cannot currently diagnose problems relating to these access bits.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Did not check unknown permissions 0x%x on '%hs' (%ws)</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Unknown access mask bits</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Security Descriptor</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_PERMS</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application was granted access to an object.</h3>
<p></p><i>Probable cause</i><p>The application was granted access to the given profile section. The profile section has not yet been analyzed for security relevance. This message is for debugging purposes only.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Ini: %hs Granted access to profile '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;INI File (profile)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Section</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Value</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Win32 Error</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;INI_PROFILE_ACCESS_GRANTED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application performed a hard administrator check.</h3>
<p></p><i>Probable cause</i><p>The application asked the operating system whether the listed SID was present in the user's access token. The SID corresponds to a privileged entity; this means that the application performs somewhat differently if the user is a member of the listed group (usually, administrators).</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Called CheckTokenMembership against trusted entity '%ws' (%hs)</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Token Handle (optional)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Binary SID</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Present?</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CHECKTOKENMEMBERSHIP_TRUSTED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called CheckTokenMembership.</h3>
<p></p><i>Probable cause</i><p>The application asked the operating system whether the listed SID was present in the user's access token. The SID was not identifiable as a trusted entity, so this message is informational only.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Called CheckTokenMembership against entity '%ws' (%hs)</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Token Handle (optional)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Binary SID</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Present?</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CHECKTOKENMEMBERSHIP_UNTRUSTED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;no</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called a WriteProfile API with LUA issue.</h3>
<p></p><i>Probable cause</i><p>The application called a WriteProfile API with parameters that might fail under standard user account.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Ini: %hs called with Ini file '%ws', Section '%ws', Key '%ws'</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;INI File (profile)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Section</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Key</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;INI_PROFILE_CONCERN</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application performed an operation that required privilege.</h3>
<p></p><i>Probable cause</i><p>The application used MAXIMUM_ALLOWED to get access required to call this function. This function would fail if called by a Standard User.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) requires '%hs' access.  This access was restricted to trusted users when the application called %hs with 'MAXIMUM_ALLOWED'.  If the application were running as a standard user, the call to %hs would succeed, but this call to %hs would fail.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle to the object being manipulated</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Name of the operation that would fail (string)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access(es) required by the operation</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Access(es) obtained for this handle that were restricted by this object's DACL</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;OP_REQUIRES_ACCESS</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The predictor was unable to query required information from a handle </h3>
<p></p><i>Probable cause</i><p>The predictor was unable to query the access granted on a handle on which the application had requested MAXIMUM_ALLOWED.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;The operating system returned unexpected error 0x%x when querying handle 0x%p</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle to the object being manipulated</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Error returned by the Operating System</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;CANNOT_QUERY_ACCESS</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application tried to launch a process that needs to run elevated on Windows Vista.</h3>
<p></p><i>Probable cause</i><p>The application tried to use CreateProcess family API to launch a process that needs to run elevated on Windows Vista. It should use ShellExecute family API instead.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs ('%ws', '%ws') tried to launch a process that needs to run elevated on Windows Vista.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;API name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Application name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Command line</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Last error code set by the API</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;ELEVATION_REQUIRED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application tried to launch a process that might need to run elevated on Windows Vista.</h3>
<p></p><i>Probable cause</i><p>The application tried to use CreateProcess family API to launch a process that might need to run elevated on Windows Vista. It should use ShellExecute family API instead.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs ('%ws', '%ws') tried to launch a process that might need to run elevated on Windows Vista.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;API name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Application name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Command line</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;ELEVATION_DETECTED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application was denied access to an object.</h3>
<p></p><i>Probable cause</i><p>The application called the listed API, which failed with an access error suggesting a potential LUA issue.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) is denied '%hs' access with error 0x%x.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error returned</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Access Requested (if applicable)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Requested (for compatibility)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;OBJECT_INACCESSIBLE</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called an API that failed unexpectedly, possibly due to bad parameters.</h3>
<p></p><i>Probable cause</i><p>The application called the listed API, which failed with an access error suggesting a potential LUA issue.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) is denied '%hs' access with error 0x%x.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Error returned</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Access Requested (if applicable)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Access Requested (for compatibility)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FAILED_API_CALL</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application opened the Security eventlog</h3>
<p></p><i>Probable cause</i><p>The application opened the Security log, which requires SE_SECURITY_PRIVILEGE to read or write. The SECURITY privilege is, by default, only granted to Administrators.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs was invoked on the (Security) Eventlog.  The Security log always requires SE_SECURITY_PRIVILEGE to access.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Eventlog Handle</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;SECURITY_LOG_OPENED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application was denied access to an object.</h3>
<p></p><i>Probable cause</i><p>The application was denied access to the given profile section due to insufficient privilege. If the application's functionality is imparied, this access problem may be the cause.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;Ini: %hs called with Ini file '%ws', Section '%ws', Key '%ws', failed with error 0x%x.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;INI File (profile)</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Section</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Key</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Error returned</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;INI_PROFILE_FAILED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application deleted a virtualized object.</h3>
<p></p><i>Probable cause</i><p>The application deleted an object (file, registry key, etc...) that the system had already designated Virtualized. This means that the next time the application attempts to open the object, it will still exist.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs called against %hs '%ws'.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;VIRTUALIZED_DELETION</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application provided unknown flags to an API.</h3>
<p></p><i>Probable cause</i><p>The application called an API with flag values that were unknown to the Verifier. The verifier analyzed the call anyway but the output may be suspect because the API may be newer than the Verifier.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs called with flags 0x%x (unknown 0x%x).</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Passed Flag Mask</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Unknown flag(s)</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Understood flag(s)</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_API_OPTIONS</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application tried to set a global Windows hook.</h3>
<p></p><i>Probable cause</i><p>The application tried to set a global Windows hook, which does not work for a standard user.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs %d (%hs) called to set a global Windows hook.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;API Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Hook Id</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread Id</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;SET_GLOBAL_HOOK</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application failed to set a Windows hook.</h3>
<p></p><i>Probable cause</i><p>The application failed to set a global Windows hook, which might be caused by inadequate privileges.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs %d (%hs) failed to set a Windows hook with error 0x%x.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;API Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Hook Id</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread Id</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Error code</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;SET_HOOK_FAILED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called NetUserGetInfo.</h3>
<p></p><i>Probable cause</i><p>The application called NetUserGetInfo and requested the user privilege information. This will work as a standard user, but it generally indicates that the application expects to be run by an administrator and is examining the access token to determine this.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;NetUserGetInfo (level: %d) called.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;User Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Level</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;NETUSERGETINFO</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called SetActivePwrScheme.</h3>
<p></p><i>Probable cause</i><p>The application called SetActivePwrScheme that might fail under standard user account.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;SetActivePwrScheme (ID: %d) called to set the active power scheme.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Power scheme Id</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Global power policy</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Power policy</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;SETACTIVEPWRSCHEME</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called SetActivePwrScheme.</h3>
<p></p><i>Probable cause</i><p>The application called SetActivePwrScheme that might fail under standard user account.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;SetActivePwrScheme (ID: %d) called to set the active power scheme and failed with error 0x%x.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Power scheme Id</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Global power policy</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Power policy</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Error code</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;SETACTIVEPWRSCHEME_FAILED</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application called AccessCheck.</h3>
<p></p><i>Probable cause</i><p>The application called AccessCheck against Builtin Administrators. It generally indicates that the application expects to be run by an administrator and is examining the access token to determine this.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;AccessCheck (%ws) called and returned AccessStatus of %d.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Sid</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;AccessStatus</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;ACCESSCHECK</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The application performed a hard admin check</h3>
<p></p><i>Probable cause</i><p>The application called the API listed above to determine if it should do something administrative. This constitutes a hard admin check.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;The application called %hs to check for administrative power.</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Successful?</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;HARDADMINCHECK</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Information: Application file name.</h3>
<p></p><i>Probable cause</i><p>Information: Application file name.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;File Name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_NAME</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Information: Application file version.</h3>
<p></p><i>Probable cause</i><p>Information: Application file version.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%d.%d.%d.%d</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;dwFileVersionMS</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;dwFileVersionLS</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_VERSION</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Information: Application file product version.</h3>
<p></p><i>Probable cause</i><p>Information: Application file product version.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%d.%d.%d.%d</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;dwProductVersionMS</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;dwProductVersionLS</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_PRODUCT_VERSION</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Information: Application file description.</h3>
<p></p><i>Probable cause</i><p>Information: Application file description.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;File description</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Language</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Code page</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_DESCRIPTION</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Information: Application file product name.</h3>
<p></p><i>Probable cause</i><p>Information: Application file product name.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;File product name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Language</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Code page</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_PRODUCT_NAME</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Information: Application file company name.</h3>
<p></p><i>Probable cause</i><p>Information: Application file company name.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;File company name</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Language</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Code page</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_COMPANY_NAME</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Information: Application file original filename.</h3>
<p></p><i>Probable cause</i><p>Information: Application file original filename.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%ws</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;File original filename</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Language</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Code page</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;FILE_ORIGINAL_FILENAME</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>
<h3>Access was restricted to elevated processes.</h3>
<p></p><i>Probable cause</i><p>The application opened an object (such as a file or registry key) and requested access permissions that were granted solely to elevated processes with high mandatory integrity label.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;%hs: %hs (%ws) only allows '%hs' access by elevated processes with high mandatory integrity label</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Object Type</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object Name</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Denied Access Bit</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;String of Denied Access Bit</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;RESTRICTED_BY_MIC</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Information: LUAPriv version.</h3>
<p></p><i>Probable cause</i><p>Information: LUAPriv version.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;LUAPriv version: %d.%d</li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Version major</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Version minor</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;n/a</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;n/a</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;LuaPriv</li>
  <li><b>Stop ID:</b>&nbsp;LUAPRIV_VERSION</li>
  <li><b>Stop code:</b>&nbsp;3300NAN</li>
  <li><b>Severity:</b>&nbsp;Info</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;no</li>
</ul>
<p></p>



 ## See Also

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Overview](application-verifier.md)

[Application Verifier - Features](application-verifier-features.md)

[Application Verifier - Testing Applications](application-verifier-testing-applications.md)
 
[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md)
  
[Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)


 





