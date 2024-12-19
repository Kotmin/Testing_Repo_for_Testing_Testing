import datetime
from typing import Protocol

# Interfaces
class TimestampGeneratorInterface(Protocol):
    def generate(self) -> datetime.datetime:
        """Generates a datetime object."""
        pass

class TimestampFormatterInterface(Protocol):
    def format(self, timestamp: datetime.datetime) -> str:
        """Formats a datetime object into a string."""
        pass

# Implementation of Generator
class SimpleTimestampGenerator(TimestampGeneratorInterface):
    def generate(self) -> datetime.datetime:
        return datetime.datetime.now(datetime.timezone.utc)

# Implementation of Formatter
class ISOFormatStrategy(TimestampFormatterInterface):
    def format(self, timestamp: datetime.datetime) -> str:
        return timestamp.isoformat()

class EpochFormatStrategy(TimestampFormatterInterface):
    def format(self, timestamp: datetime.datetime) -> str:
        return str(int(timestamp.timestamp()))

class RFC1123FormatStrategy(TimestampFormatterInterface):
    def format(self, timestamp: datetime.datetime) -> str:
        return timestamp.strftime("%a, %d %b %Y %H:%M:%S GMT")

# Service combining generator and formatter
class TimestampService:
    def __init__(self, generator: TimestampGeneratorInterface, formatter: TimestampFormatterInterface):
        self.generator = generator
        self.formatter = formatter

    def get_formatted_timestamp(self) -> str:
        timestamp = self.generator.generate()
        return self.formatter.format(timestamp)

# Main function to demonstrate usage
def main():
    # Create generator and formatters
    generator = SimpleTimestampGenerator()

    iso_formatter = ISOFormatStrategy()
    epoch_formatter = EpochFormatStrategy()
    rfc_formatter = RFC1123FormatStrategy()

    # ISO Format
    iso_service = TimestampService(generator, iso_formatter)
    print(f"ISO 8601: {iso_service.get_formatted_timestamp()}")

    # Unix Epoch Format
    epoch_service = TimestampService(generator, epoch_formatter)
    print(f"Epoch: {epoch_service.get_formatted_timestamp()}")

    # RFC 1123 Format
    rfc_service = TimestampService(generator, rfc_formatter)
    print(f"RFC 1123: {rfc_service.get_formatted_timestamp()}")

if __name__ == "__main__":
    main()
