# import logging
# logger = logging.getLogger(__name__)
# handler = logging.StreamHandler()

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# handler.setFormatter(formatter)

# logger.addHandler(handler)
# logger.setLevel(logging.INFO)

# def divide(dividend, divisor):
#     try:
#         logger.info(f"Dividing {dividend} by {divisor}")
#         return dividend/divisor
#     except ZeroDivisionError:
#         logger.info("zero division error")
# print(divide(6,0))



import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)

def divide(dividend, divisor):
    try:
        logger.info(f"Dividing {dividend} by {divisor}")
        return dividend/divisor
    except ZeroDivisionError:
        logger.info("zero division error")


print(divide(6,2))