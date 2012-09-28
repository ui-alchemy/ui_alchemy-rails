## ConvergeUI Contribution Workflow

1. Fork the upstream repository

2. Create a feature branch related to the bug or feature in your fork

3. Commit code to your branch and push to your fork
 * Ensure your code follows the style and naming conventions:
   * [SCSS](http://docs.convergeui.org/en/latest/resources/stylesheets.html#scss-code-conventions)
   * [JavaScript](http://docs.convergeui.org/en/latest/resources/javascript.html#project-javascript-code-conventions)
 * Preface the commit messages with the issue number or feature and include a brief message, e.g.
````
	34 - Fixes ie bug that caused no background colors to be shown.

	or

	Header Updates - Adds dropdown menu in tabs to be used as a application context switcher.
````

4. Open a pull request on the upstream repository and include:
 * brief description of the issue being fixed or feature being added
 * explanation of approach taken when warranted
 * references or links to visual implementation of feature e.g. codepen, converge-ui-example, screenshot
 * decide if you would like specific individuals to review your request and include them via the @-tag e.g. @ehelms


5. The pull request will be assigned an iteration that fits the current release schedule.

6. A reviewer will be assigned who is responsible for merging under the following conditions:
 * If no specific reviewers have been requested, the assigned reviewer may ACK and merge at will
 * If specific reviewers have been requested via @-tag, reviewer may ACK and merge after all requested reviewers have ACK\'d
 * If there are comments raised by others within the pull request, reviewer should ensure the concerns have been met and request ACKs from those who commented on the pull request before ACK'ing and merging
