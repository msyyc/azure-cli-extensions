# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['spatial-anchors-account'] = """
    type: group
    short-summary: Manage spatial anchor account with mixedreality
"""

helps['spatial-anchors-account list'] = """
    type: command
    short-summary: "List Resources by Resource Group And List Spatial Anchors Accounts by Subscription."
    examples:
      - name: List spatial anchor accounts by resource group
        text: |-
               az spatial-anchors-account list --resource-group "MyResourceGroup"
      - name: List spatial anchors accounts by subscription
        text: |-
               az spatial-anchors-account list
"""

helps['spatial-anchors-account show'] = """
    type: command
    short-summary: "Retrieve a Spatial Anchors Account."
    examples:
      - name: Get spatial anchors account
        text: |-
               az spatial-anchors-account show --account-name "MyAccount" --resource-group \
"MyResourceGroup"
"""

helps['spatial-anchors-account create'] = """
    type: command
    short-summary: "Creating or Updating a Spatial Anchors Account."
    parameters:
      - name: --sku
        short-summary: "The sku associated with this account"
        long-summary: |
            Usage: --sku name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
      - name: --kind
        short-summary: "The kind of account, if supported"
        long-summary: |
            Usage: --kind name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
    examples:
      - name: Create spatial anchor account
        text: |-
               az spatial-anchors-account create --account-name "MyAccount" --resource-group "MyResourceGroup"
"""

helps['spatial-anchors-account update'] = """
    type: command
    short-summary: "Updating a Spatial Anchors Account."
    parameters:
      - name: --sku
        short-summary: "The sku associated with this account"
        long-summary: |
            Usage: --sku name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
      - name: --kind
        short-summary: "The kind of account, if supported"
        long-summary: |
            Usage: --kind name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
    examples:
      - name: Update spatial anchors account
        text: |-
               az spatial-anchors-account update --account-name "MyAccount" --resource-group \
"MyResourceGroup" --location "eastus2euap" --tags hero="romeo" heroine="juliet"
"""

helps['spatial-anchors-account delete'] = """
    type: command
    short-summary: "Delete a Spatial Anchors Account."
    examples:
      - name: Delete spatial anchors account
        text: |-
               az spatial-anchors-account delete --account-name "MyAccount" --resource-group \
"MyResourceGroup"
"""

helps['spatial-anchors-account key show'] = """
    type: command
    short-summary: "List Both of the 2 Keys of a Spatial Anchors Account."
    examples:
      - name: List spatial anchor account key
        text: |-
               az spatial-anchors-account key show --account-name "MyAccount" --resource-group \
"MyResourceGroup"
"""

helps['spatial-anchors-account key renew'] = """
    type: command
    short-summary: "Regenerate specified Key of a Spatial Anchors Account."
    examples:
      - name: Regenerate spatial anchors account keys
        text: |-
               az spatial-anchors-account key renew --account-name "MyAccount" --serial 1 \
--resource-group "MyResourceGroup"
"""

helps['remote-rendering-account'] = """
    type: group
    short-summary: Manage remote rendering account with mixedreality
"""

helps['remote-rendering-account list'] = """
    type: command
    short-summary: "List Resources by Resource Group And List Remote Rendering Accounts by Subscription."
    examples:
      - name: List remote rendering accounts by resource group
        text: |-
               az remote-rendering-account list --resource-group "MyResourceGroup"
      - name: List remote rendering accounts by subscription
        text: |-
               az remote-rendering-account list
"""

helps['remote-rendering-account show'] = """
    type: command
    short-summary: "Retrieve a Remote Rendering Account."
    examples:
      - name: Get remote rendering account
        text: |-
               az remote-rendering-account show --account-name "MyAccount" --resource-group \
"MyResourceGroup"
"""

helps['remote-rendering-account create'] = """
    type: command
    short-summary: "Creating or Updating a Remote Rendering Account."
    parameters:
      - name: --sku
        short-summary: "The sku associated with this account"
        long-summary: |
            Usage: --sku name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
      - name: --kind
        short-summary: "The kind of account, if supported"
        long-summary: |
            Usage: --kind name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
    examples:
      - name: Create remote rendering account
        text: |-
               az remote-rendering-account create --account-name "MyAccount" --location "eastus2euap" \
--resource-group "MyResourceGroup"
"""

helps['remote-rendering-account update'] = """
    type: command
    short-summary: "Updating a Remote Rendering Account."
    parameters:
      - name: --sku
        short-summary: "The sku associated with this account"
        long-summary: |
            Usage: --sku name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
      - name: --kind
        short-summary: "The kind of account, if supported"
        long-summary: |
            Usage: --kind name=XX tier=XX size=XX family=XX capacity=XX

            name: Required. The name of the SKU. Ex - P3. It is typically a letter+number code
            tier: This field is required to be implemented by the Resource Provider if the service has more than one \
tier, but is not required on a PUT.
            size: The SKU size. When the name field is the combination of tier and some other value, this would be the \
standalone code.
            family: If the service has different generations of hardware, for the same SKU, then that can be captured \
here.
            capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in \
is not possible for the resource this may be omitted.
    examples:
      - name: Update remote rendering account
        text: |-
               az remote-rendering-account update --account-name "MyAccount" --tags hero="romeo" heroine="juliet" \
--resource-group "MyResourceGroup"
"""

helps['remote-rendering-account delete'] = """
    type: command
    short-summary: "Delete a Remote Rendering Account."
    examples:
      - name: Delete remote rendering account
        text: |-
               az remote-rendering-account delete --account-name "MyAccount" --resource-group \
"MyResourceGroup"
"""

helps['remote-rendering-account key show'] = """
    type: command
    short-summary: "List Both of the 2 Keys of a Remote Rendering Account."
    examples:
      - name: List remote rendering account key
        text: |-
               az remote-rendering-account key show --account-name "MyAccount" --resource-group \
"MyResourceGroup"
"""

helps['remote-rendering-account key renew'] = """
    type: command
    short-summary: "Regenerate specified Key of a Remote Rendering Account."
    examples:
      - name: Regenerate remote rendering account keys
        text: |-
               az remote-rendering-account key renew --account-name "MyAccount" --serial 1 \
--resource-group "MyResourceGroup"
"""

helps['spatial-anchors-account key'] = """
    type: group
    short-summary: Manage developer keys of a Spatial Anchors Account.
"""

helps['remote-rendering-account key'] = """
    type: group
    short-summary: Manage developer keys of a Remote Rendering Account.
"""
