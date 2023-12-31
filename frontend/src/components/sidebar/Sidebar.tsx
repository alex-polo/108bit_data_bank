import { ReactElement } from 'react';

import styles from './Sidebar.module.css';
import { Nav } from 'react-bootstrap';

function Sidebar(): ReactElement {
  return (
    <>
      <div className={styles.sidebar}>
        Data Bank
        <Nav defaultActiveKey="/home" className="flex-column">
          <Nav.Link href="/home">Active</Nav.Link>
          <Nav.Link eventKey="link-1">Link</Nav.Link>
          <Nav.Link eventKey="link-2">Link</Nav.Link>
          <Nav.Link eventKey="disabled" disabled>
            Disabled
          </Nav.Link>
        </Nav>
      </div>
    </>
  );
}

export default Sidebar;
