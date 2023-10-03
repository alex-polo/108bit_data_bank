import { Alert, Container } from 'react-bootstrap';
import { isRouteErrorResponse, useRouteError } from 'react-router-dom';

const ErrorPage: React.FC = () => {
  const error = useRouteError();
  console.error(error);

  let errorMessage = '';

  if (isRouteErrorResponse(error)) {
    errorMessage = `Return code: ${error.status}. Message: ${error.statusText}, ${error.data}.`;
  } else if (error instanceof Error) {
    errorMessage = error.message;
  } else if (typeof error === 'string') {
    errorMessage = error;
  } else {
    console.error(error);
    errorMessage = 'Unknown error';
  }

  return (
    <div id="error-page">
      <Container>
        <Alert variant="success">
          <Alert.Heading>Oops!</Alert.Heading>

          <p>Sorry, an unexpected error has occurred.</p>
          <hr />
          <p className="mb-0">{errorMessage}</p>
        </Alert>
      </Container>
    </div>
  );
};

export default ErrorPage;
