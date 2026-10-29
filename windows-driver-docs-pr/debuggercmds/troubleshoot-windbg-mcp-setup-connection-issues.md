---
title: Troubleshoot WinDbg MCP
description: Resolve WinDbg MCP registration, session connection, access, and prompt-injection protection issues with supported AI clients.
ms.date: 09/24/2026
ms.topic: troubleshooting-general
ai-usage: ai-assisted

#customer intent: As a Windows debugger user, I want to resolve WinDbg MCP setup and connection issues so that I can connect a supported AI client to the intended debugging session.
---

# Troubleshoot WinDbg MCP setup and connection issues

Use this article when Visual Studio Code with GitHub Copilot or GitHub Copilot CLI can't register the WinDbg Model Context Protocol (MCP) server, can't connect to a WinDbg MCP session, or WinDbg MCP security controls block an operation. Registering adds the WinDbg MCP server to the AI client's configuration, while connecting associates the client with a specific WinDbg session.

For setup instructions, see [Install and enable WinDbg MCP](set-up-windbg-mcp.md#install-and-enable-windbg-mcp). For authoritative security and privacy guidance, see [WinDbg MCP security and privacy considerations](windbg-mcp-overview.md#windbg-mcp-security-and-privacy-considerations).

Start with the symptom that you observe, identify the likely cause, and complete the resolution steps.

## Troubleshooting checklist

For MCP server registration issues:

1. Open WinDbg. You don't need to load or attach to a debugging target to use **Enable Server** or **Install MCP**.
1. Open **MCP service settings**, and confirm that you selected **Enable Server**.
1. Confirm that you selected Visual Studio Code or GitHub Copilot CLI as the client.

For connection or session issues:

1. Start **MCP Service** in the intended WinDbg window.
1. If you're analyzing a target, load or attach to the debugging target as needed.

## The MCP server list doesn't include WinDbg

The supported AI client's MCP server list doesn't include WinDbg.

### Cause

**Install MCP** didn't register WinDbg with the client, or the client hasn't reloaded its MCP server configuration.

### Resolution

1. Restart the AI client, and then check its MCP server list.
1. In WinDbg, open **MCP service settings** and select the correct supported client.
1. Select **Install MCP** again.
1. Complete any confirmation that the client displays.
1. Restart the client, and then check its MCP server list again.

If WinDbg is still missing because **Install MCP** fails, register WinDbg manually.

### Register a supported client manually

Use this fallback only when **Install MCP** doesn't register WinDbg with Visual Studio Code or GitHub Copilot CLI.

1. In WinDbg, open **MCP service settings**.
1. Select **Custom** to display the proxy configuration. Selecting **Custom** in this step only provides the proxy command for the supported-client configuration.
1. Select **Copy to Clipboard**, and note the `command` path that WinDbg copies to the clipboard.

Configure the supported client:

#### [Visual Studio Code](#tab/visual-studio-code)

1. In your workspace, add the WinDbg server to `.vscode/mcp.json`. Replace the example `command` value with the path from the clipboard:

   ```json
   {
     "servers": {
       "WinDbg": {
         "type": "stdio",
         "command": "C:\\path\\to\\DbgX.Mcp.Proxy.exe",
         "args": []
       }
     }
   }
   ```

1. Restart Visual Studio Code.

#### [GitHub Copilot CLI](#tab/command-line)

1. Add an MCP server and name it `WinDbg`. Replace the example proxy path with the `command` path from the clipboard:

   ```console
   copilot mcp add WinDbg -- "C:\path\to\DbgX.Mcp.Proxy.exe"
   ```

1. Restart GitHub Copilot CLI.

---

After the client restarts, see [Verify the WinDbg MCP connection](set-up-windbg-mcp.md#verify-the-windbg-mcp-connection).

## GitHub Copilot can't find the intended WinDbg session

Visual Studio Code with GitHub Copilot and GitHub Copilot CLI can't find the WinDbg session that contains the intended debugging target.

### Cause

**MCP Service** isn't running in the intended WinDbg window, or more than one WinDbg session is available and the proxy can't select a session automatically.

### Resolution

1. In the intended WinDbg window, select **MCP Service**.
1. Ask the AI client to use `list_sessions`.
1. Identify the process ID for the intended WinDbg session.
1. Ask the AI client to use `connect_session` with that process ID.
1. Confirm that the target type and execution state that the client reports match those in the intended WinDbg window.

For more session-selection guidance, see [Manage WinDbg sessions](set-up-windbg-mcp.md#manage-windbg-sessions).

## WinDbg session is unavailable because another client is connected

The intended WinDbg session appears unavailable when the AI client lists sessions or tries to connect.

### Cause

Another AI client has an active connection to the WinDbg session. Only one active MCP client can connect to a WinDbg session at a time.

### Resolution

1. In the connected AI client, ask the client to use `disconnect_session`.
1. Confirm that the client reports that it disconnected from the WinDbg session.
1. In the intended AI client, ask the client to use `list_sessions`.
1. Ask the intended client to use `connect_session` with the WinDbg session's process ID.
1. Confirm that the client reports a connection to the intended session.

## Access denied when WinDbg is elevated

The connection fails with an **Access denied** message when WinDbg is running as an administrator.

### Cause

The elevated WinDbg session prevents the supported AI client from connecting through the proxy.

### Resolution

1. Close the elevated WinDbg session.
1. Start WinDbg without selecting **Run as administrator**.
1. Start **MCP Service**.
1. Load or attach to the debugging target as needed.
1. Open the supported AI client, and complete the steps in [Verify the WinDbg MCP connection](set-up-windbg-mcp.md#verify-the-windbg-mcp-connection).

## Prompt-injection protection blocks an operation

The AI client reports that prompt-injection protection blocked an operation or classified debugger output as unsafe.

### Cause

WinDbg cross-prompt injection attack (XPIA) protection identified the debugger output as potentially unsafe and blocked the output.

### Resolution

1. Follow the error information that the AI client reports.
1. Review the relevant output directly in WinDbg.
1. Treat the output as untrusted, and don't send the blocked output to the AI client.
1. Review [Cross-prompt injection protection](windbg-mcp-overview.md#cross-prompt-injection-protection) before you decide how to continue.

## Prompt-injection classification can't run because the AI client doesn't support or permit MCP sampling

The AI client reports that prompt-injection classification can't run, and the protected operation fails without returning output.

### Cause

The AI client doesn't support MCP sampling, or its configuration or organizational policy doesn't permit MCP sampling. WinDbg XPIA protection requires MCP sampling to request classification from the client's configured model service.

### Resolution

1. Confirm that the AI client supports MCP sampling.
1. Confirm that the client configuration and your organizational policy permit MCP sampling.
1. After sampling is available, run the operation again.
1. If classification still can't run, review [Cross-prompt injection protection](windbg-mcp-overview.md#cross-prompt-injection-protection) and contact the administrator who manages the AI client's policy.

## Verify the WinDbg MCP connection and report unresolved issues

- [Verify the WinDbg MCP connection](set-up-windbg-mcp.md#verify-the-windbg-mcp-connection).
- Review the [WinDbg MCP security and privacy considerations](windbg-mcp-overview.md#windbg-mcp-security-and-privacy-considerations).
- If the issue continues, report it in the [WinDbg Feedback repository](https://github.com/microsoft/WinDbg-Feedback/issues).
