# -*- coding: utf-8 -*-
"""
psearch.utils.misc
~~~~~~~~~~~~~~~~~~

This module contains various utility functions and tiny wrappers around
vim functions.
"""

import os
import vim


def echom(msg):
    """To display a simple feedback to the user via the command line."""
    vim.command('echom "[pse] {0}"'.format(msg))


def echoerr(msg):
    """To display a simple error feedback to the user via the command line."""
    vim.command('echohl WarningMsg|echom "[pse] {0}"|echohl None'.format(
        msg.replace('"', '\"')))


def redraw():
    """Little wrapper around the redraw command."""
    vim.command('redraw')


def set_buffer(lst):
    """To set the whole content of the current buffer at once."""
    vim.current.buffer[:] = lst


def bufwinnr(identifier):
    """To return the number of the window whose buffer is named or numbered
    'identifier'."""
    if isinstance(identifier, (int, long)):
        nr = int(vim.eval("bufwinnr({0})".format(identifier)))
    else:
        nr = int(vim.eval("bufwinnr('{0}')".format(identifier)))
    return nr if nr > 0 else 0


def bufname(number=None):
    """To return the name of the buffer(default - current buffer)."""
    if number:
        return vim.eval("bufname({0})".format(number))
    else:
        return vim.eval("bufname('%')")


def winnr():
    """To return the current window number."""
    return vim.eval('winnr()')


def go_to_win(nr):
    """To go to the window with the given number."""
    vim.command('{0}wincmd w'.format(nr))


def buffers():
    """To return a list of all listed and named buffers."""
    return [b.number for b in vim.buffers
            if b.name and int(vim.eval("buflisted({0})".format(b.number)))]
