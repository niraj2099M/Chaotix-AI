from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import image_gen_worker


# Create your views here.

@api_view(['POST'])
def image_gen(request):
    """
    This function handles image generation requests.

    Args:
        request (HttpRequest): The HTTP request object containing the image prompt data.

    Returns:
        HttpResponse: A response containing the IDs of the created image generation tasks
                      or an error message.
    """

    try:
        # Extract the list of prompts from the request data
        prompts = request.data.get("prompts")

        # Check if prompts are provided
        if not prompts:
            return Response({"error": "Missing prompts in request data"}, status=400)

        # Create a list to store task IDs
        task_ids = []

        # Loop through each prompt and call the image_gen_worker task asynchronously
        for prompt in prompts:
            task_id = image_gen_worker.delay(prompt).id  # Delay for asynchronous execution
            task_ids.append(task_id)

        # Return a response with the list of generated task IDs
        return Response({"task_ids": task_ids})
    except Exception:
        # Handle any unexpected errors
        return Response("INTERNAL SERVER ERROR", status=500)
