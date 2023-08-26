from recordbook.record_classes import PhoneException, BirthdayException, EmailException
from functools import wraps


# Декоратор для Обробки командної строки
def input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            result = func(*args)

        except BirthdayException as e:
            result = f"{e}\n {func.__doc__}"
        except PhoneException as e:
            result = f"{e}\n {func.__doc__}"
        except EmailException as e:
            result = f"{e}\n {func.__doc__}"
        except FileNotFoundError:
            result = f"The database is not found\n {func.__doc__}"
        except ValueError:
            result = f"Incorect data or unsupported format while writing to the file\n {func.__doc__}"
        except KeyError:
            result = f"Record is not in the database\n {func.__doc__}"
        except TypeError:
            result = f"Incorect data\n {func.__doc__}"
        except IndexError:
            result = func.__doc__
        return result

    return inner
