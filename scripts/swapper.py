#!/bin/python3
"""Swap and unswap between a container and the biggest container in the workspace."""
from typing import Tuple
import i3ipc

# NOTE: for documentation look in: https://github.com/altdesktop/i3ipc-python
# for this to work you need python3 and i3ipc installed on your machine.
# Install it with pip3 install i3ipc.

# Initiate i3ipc library.
i3 = i3ipc.Connection()

# We need tree of containers to find focused and the biggest one.
tree = i3.get_tree()

# Class of currently focused container.
focused = tree.find_focused()

# Check if focused is floating.
# Possible states are: 'auto_on', 'auto_off', 'user_on', 'user_off'
focused_floating_state = "on" in focused.floating

# List of containers on focused workspace.
list_con = focused.workspace().leaves()


def get_info(list_con) -> Tuple[str, str]:
    """
    Retrieve required information from the list of containers

    This is a tuple with:

        1. ID of the largest container (by area)
        2. ID of the focused container
    """

    largest = 0
    largest_container = list_con[0]
    focused_container = ""
    for container in list_con:
        y = container.rect.height
        x = container.rect.width
        if x * y >= largest:
            largest = x * y
            largest_container = container
        if container.focused:
            focused_container = container

    return largest_container.id, focused_container.id


def get_latest_container_swapped():
    """Get the ID of the non-focues container that was last swapped."""
    marks = i3.get_marks()
    for mark in marks:
        if mark.startswith("latest_"):
            return mark.replace("latest_", "")


# Get swappin'
if focused_floating_state:  # If currently focused is floating, do nothing.
    pass
else:
    largest_con_id, focused_container = get_info(list_con)
    latest_swapped = get_latest_container_swapped()
    marks = i3.get_marks()

    # Focus is on the big one but there has been a swap before
    if largest_con_id == focused_container and any("latest_" in mark for mark in marks):
        container_to_swap = get_latest_container_swapped()
        i3.command(f"swap container with con_id {container_to_swap}")
    # No previous swaps and the focus is in the biggest container
    elif largest_con_id == focused_container:
        pass
    # Focus is on not the biggest one
    elif largest_con_id != focused_container:
        i3.command(f"swap container with con_id {largest_con_id}")
        i3.command(f"mark --replace latest_{largest_con_id}")
