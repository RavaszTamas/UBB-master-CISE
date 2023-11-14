import lmql


__CONTEXT_STUDY_AID = """
You are work aiding chatbot that generates FASTApi endpoints based on Pydnatic shcemas.
You will get a couple of Pydantic schemas from which you have to create FASTApi endpoints.
""".strip()


@lmql.query
def synthesize_data() -> lmql.LMQLResult:
    '''lmql
    import numpy as np

    ENPDOINT_TYPES = ["get", "put", "delete", "post"]

    usecase = np.random.choice(["car salesmanship", "advertisement", "construction", "IT networking", "education", "mining", "infrastructure development", "sport betting", "stock trading", "3D printing", "video game buying"])

    sample(temperature=0.2)
        """
        Create five Pydantic schemas to {usecase} use case!
        """
        NUMBER_OF_OBJECTS = np.random.randint(3, 5)
        for _ in range(NUMBER_OF_OBJECTS):
            """
            class [PYDANTIC_SCHEMA_NAME]:
            """
            NUMBER_OF_PARAMETERS = np.random.randint(2, 4)
            for _ in range(NUMBER_OF_PARAMETERS):
                """[PARAM_ONE]: [TYPE_ONE]\n"""

        """Implement CRUD functions for the schemas above in Python with FastAPI using a Redis database! Strictly include the program code! Add a get and get all endpoint as well to the put delete and update endpoints! The get all method should use accurate Redis calls! Do not use unicode characters, only utf-8 characters!\n"""
        NUMBER_OF_ENDPOINTS = np.random.randint(2, 4)
        for _ in range(NUMBER_OF_ENDPOINTS):
            ENPOINT_TYPE = np.random.choice(ENPDOINT_TYPES)
            """
            @index_router.{ENPOINT_TYPE}([ENDPOINT])
            [FASTAPI_CRUD_FUNCTION]
            \n
            """
    from
        "openai/gpt-3.5-turbo-instruct"
    where
        STOPS_BEFORE(PYDANTIC_SCHEMA_NAME, ":") or STOPS_BEFORE(PARAM_ONE, ":") or STOPS_BEFORE(TYPE_ONE, "\n") or  STOPS_BEFORE(ENDPOINT, ")") or STOPS_BEFORE(FASTAPI_CRUD_FUNCTION, "\n\n")  
    '''

@lmql.query
async def generate_code(
    pydantic_schemas:str,
    used_model:str,
    __context=__CONTEXT_STUDY_AID,
) -> lmql.LMQLResult:
    '''lmql
    import numpy as np
    ENPDOINT_TYPES = ["get", "put", "delete", "post"]

    sample(temperature=0.2)
        """Implement CRUD functions for the Pydantic schemas below with FastAPI using a Redis database!

        {pydantic_schemas}

        Strictly include the program code! Add a 'get' and 'get_all' endpoint as well besides the 'put', 'delete' and 'update' endpoints! The 'get_all' method should use accurate Redis calls! Be specific as you can be even in text formatting! Only use utf-8 characters!\n"""
        '[FASTAPI_CRUD_FUNCTION]$$\n'

            
    from
        used_model
    where
        STOPS_BEFORE(FASTAPI_CRUD_FUNCTION, "$$")  
    '''

# @lmql.query
# async def make_summary(
#     sources: List[str],
#     used_model: str,
#     __context=__CONTEXT_STUDY_AID,
# ) -> lmql.LMQLResult:
#     '''lmql
#     sample(temperature=0.4)
#         """
#         {__context}
#         The book sources are:\n
#         """
#         for i, s in enumerate(sources):
#             "[[{i}]]: {s}\n\n"
#         """
#         Summarize the sources above in a clean and easy to read way! Try to reduce the length of the generated text compared to the sources, but retain as much important information as you can!
#         """
#         "[OUTPUT]$$\n"
#         "On a scale from 0.0% to 100.0% from information point of view the summary retained [SUMM_RETENTION_PCT]% of the sources!"
#     from
#         used_model
#     where
#         STOPS_AT(OUTPUT, "$$") or STOPS_AT(SUMM_RETENTION_PCT, "%")
#     '''
