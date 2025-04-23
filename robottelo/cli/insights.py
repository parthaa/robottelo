"""
Usage:
    hammer insights [OPTIONS] SUBCOMMAND [ARG] ...

Parameters:
 SUBCOMMAND                    Subcommand
 [ARG] ...                     Subcommand arguments

Subcommands:
 cloud-connector               Manage cloud connector setup
 inventory                     Manage inventory related operations

Options:
 -h, --help                    Print help

"""

from nailgun import client

from robottelo.cli.base import Base
from robottelo.config import get_credentials, get_url


class Insights(Base):
    """
    Exports content from satellite
    """

    command_base = 'insights'
    command_requires_org = True

    @classmethod
    def inventorySync(cls, options):
        """
        Start inventory status sync
        """
        cls.command_sub = 'inventory sync'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def inventoryGenerateReport(cls, options):
        """
        Start new report generation
        """
        cls.command_sub = 'inventory generate-report'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def inventoryDownloadReport(cls, options):
        """
        Download the last generated report
        """
        cls.command_sub = 'inventory download-report'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def cloudConnectorEnable(cls, options=None):
        """
        Enable cloud connector
        """
        cls.command_sub = 'cloud-connector enable'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def fetchLastUploadLog(cls, options):
        url = f'{get_url()}/foreman_inventory_upload/{options["organization-id"]}/uploads/last'
        headers = {"Accept": "application/json"}
        return client.get(url, auth=get_credentials(), headers=headers, verify=False).json()

    @classmethod
    def fetchLastReportLog(cls, options):
        url = f"{get_url()}/foreman_inventory_upload/{options['organization-id']}/reports/last"
        headers = {"Accept": "application/json"}
        return client.get(url, auth=get_credentials(), headers=headers, verify=False).json()
